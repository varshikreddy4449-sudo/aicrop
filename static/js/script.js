/**
 * AgriAI - Core Client Engine
 * - Multi-Language Text-To-Speech (English, Hindi, Telugu)
 * - Drag-and-Drop Leaf Image Upload with Instant Preview & Validation
 * - Quick-Test Agronomic Presets for Easy Evaluation
 */

(function () {
  'use strict';

  // ── Active Language Detection Helper ────────────────────────────────────
  function getActiveLanguage() {
    return (document.documentElement.lang || window.CURRENT_LANG || 'en').toLowerCase().trim();
  }

  // ── 1. Text-To-Speech (TTS) Engine ─────────────────────────────────────
  class AgriAudioEngine {
    constructor() {
      this.synth = window.speechSynthesis || null;
      this.currentUtterance = null;
      this.activeButton = null;
      this.lastSpokenText = '';
      this.lastSpokenLang = 'en';
      this.isPlaying = false;
      this.voices = [];
      this.noticeTimer = null;

      if (this.synth) {
        this.loadVoices();
        if (typeof this.synth.onvoiceschanged !== 'undefined') {
          this.synth.onvoiceschanged = () => {
            this.loadVoices();
          };
        }
      }
      this.createFloatingAudioBar();
    }

    loadVoices() {
      if (!this.synth) return [];
      this.voices = this.synth.getVoices() || [];
      return this.voices;
    }

    /**
     * Check if a specific language voice is available on this client/OS.
     */
    hasVoiceForLanguage(langCode) {
      return Boolean(this.getVoiceForLanguage(langCode));
    }

    /**
     * Selects voice strictly matching requested language.
     * For Telugu (te-IN), it strictly finds a voice starting with 'te' or named Telugu.
     * It NEVER silently falls back to English or Hindi for Telugu.
     */
    getVoiceForLanguage(langCode) {
      const voices = this.loadVoices();
      if (!voices || voices.length === 0) return null;

      const code = (langCode || 'en').toLowerCase().trim();

      // TELUGU (te-IN): Strictly match te-IN or voice starting with te
      if (code === 'te' || code.startsWith('te-')) {
        return voices.find(v => {
          const l = (v.lang || '').toLowerCase().replace('_', '-');
          const n = (v.name || '').toLowerCase();
          return l === 'te-in' || l.startsWith('te-') || l === 'te' || n.includes('telugu');
        }) || null;
      }

      // HINDI (hi-IN): Strictly match hi-IN or voice starting with hi
      if (code === 'hi' || code.startsWith('hi-')) {
        return voices.find(v => {
          const l = (v.lang || '').toLowerCase().replace('_', '-');
          const n = (v.name || '').toLowerCase();
          return l === 'hi-in' || l.startsWith('hi-') || l === 'hi' || n.includes('hindi');
        }) || null;
      }

      // ENGLISH: Prefer en-IN (Indian English), fallback to other English voices
      if (code === 'en' || code.startsWith('en-')) {
        const indianEnglish = voices.find(v => {
          const l = (v.lang || '').toLowerCase().replace('_', '-');
          const n = (v.name || '').toLowerCase();
          return l === 'en-in' || n.includes('india') || n.includes('heera') || n.includes('ravi') || n.includes('neerja');
        });
        if (indianEnglish) return indianEnglish;

        const anyEnglish = voices.find(v => {
          const l = (v.lang || '').toLowerCase().replace('_', '-');
          return l.startsWith('en-') || l === 'en';
        });
        if (anyEnglish) return anyEnglish;

        return voices.find(v => v.default) || voices[0] || null;
      }

      return null;
    }

    /**
     * Cleans raw text: removes buttons, navigation, speaker labels, duplicate headings,
     * emojis, and converts units into smooth natural spoken phrases.
     */
    cleanTextForSpeech(text, lang = 'en') {
      if (!text) return '';

      let clean = String(text);

      // 1. Remove HTML tags
      clean = clean.replace(/<[^>]*>?/gm, ' ');

      // 2. Remove emojis and common UI icon glyphs
      clean = clean.replace(/[\u{1F300}-\u{1FAFF}\u{2600}-\u{26FF}\u{2700}-\u{27BF}✓⚠️🛡️🗓️🌱🌡️💧🧪🌧️🔬👁️💊🌿🔊⏹️🔁📢🏠📊🌾🍃📜🚪🌐]/gu, ' ');

      // 3. Remove speaker, audio, button, and navigation action labels
      clean = clean.replace(/\b(listen|replay|stop|play|audio|btn_listen|model output|ai recommendation|scanned leaf|prediction result|glass-panel)\b/gi, ' ');
      clean = clean.replace(/\b(सुनें|रोकें|पुनः सुनें|ऑडियो)\b/gi, ' ');
      clean = clean.replace(/\b(వినండి|ఆపండి|మళ్ళీ వినండి|ఆడియో)\b/gi, ' ');

      // 4. Natural conversions for units and percentages
      if (lang === 'te' || lang.startsWith('te')) {
        clean = clean.replace(/(\d+(\.\d+)?)\s*%/g, '$1 శాతం');
        clean = clean.replace(/(\d+(\.\d+)?)\s*°\s*C/gi, '$1 డిగ్రీల సెల్సియస్');
        clean = clean.replace(/(\d+(\.\d+)?)\s*mm/gi, '$1 మిల్లీమీటర్లు');
        clean = clean.replace(/\bpH\s*(\d+(\.\d+)?)/gi, 'పీహెచ్ $1');
      } else if (lang === 'hi' || lang.startsWith('hi')) {
        clean = clean.replace(/(\d+(\.\d+)?)\s*%/g, '$1 प्रतिशत');
        clean = clean.replace(/(\d+(\.\d+)?)\s*°\s*C/gi, '$1 डिग्री सेल्सियस');
        clean = clean.replace(/(\d+(\.\d+)?)\s*mm/gi, '$1 मिलीमीटर');
        clean = clean.replace(/\bpH\s*(\d+(\.\d+)?)/gi, 'पीएच $1');
      } else {
        clean = clean.replace(/(\d+(\.\d+)?)\s*%/g, '$1 percent');
        clean = clean.replace(/(\d+(\.\d+)?)\s*°\s*C/gi, '$1 degrees Celsius');
        clean = clean.replace(/(\d+(\.\d+)?)\s*mm/gi, '$1 millimeters');
        clean = clean.replace(/\bpH\s*(\d+(\.\d+)?)/gi, 'pH $1');
      }

      // 5. Convert bullet marks and list separators into natural pauses
      clean = clean.replace(/[•*▪▫\t\r]+/g, ', ');
      clean = clean.replace(/\s*;\s*/g, ', ');
      clean = clean.replace(/:\s+/g, ': ');

      // 6. Remove duplicate punctuation and excessive whitespace
      clean = clean.replace(/\s+/g, ' ');
      clean = clean.replace(/([.,])\s*([.,])+/g, '$1');

      return clean.trim();
    }

    /**
     * Extracts complete prediction information from the active page
     * and formats it into a single, natural, conversational advisory narrative.
     */
    buildConversationalSpeech(triggerEl, fallbackRawText, lang) {
      // ── A. Check for Crop Recommendation Result on Page ──
      const cropPanel = document.querySelector('.info-cards-grid');
      const cropHeader = document.querySelector('h1.display-5');

      if (cropPanel && cropHeader) {
        const cropName = cropHeader.textContent.trim();

        // Extract confidence
        const confBadge = document.querySelector('.confidence-bar-wrapper')?.previousElementSibling?.querySelector('.fw-bold');
        const confidence = confBadge ? confBadge.textContent.replace('%', '').trim() : '';

        // Extract agronomic cards
        const cards = document.querySelectorAll('.info-cards-grid .info-card');
        let season = '', soil = '', temp = '', hum = '', ph = '', rain = '';

        cards.forEach(card => {
          const label = (card.querySelector('.info-card-label')?.textContent || '').toLowerCase();
          const val = card.querySelector('.info-card-val')?.textContent?.trim() || '';
          if (label.includes('season') || label.includes('मौसम') || label.includes('కాలం')) season = val;
          else if (label.includes('soil') || label.includes('मिट्टी') || label.includes('నేల')) soil = val;
          else if (label.includes('temperature') || label.includes('तापमान') || label.includes('ఉష్ణోగ్రత')) temp = val;
          else if (label.includes('humidity') || label.includes('आर्द्रता') || label.includes('తేమ')) hum = val;
          else if (label.includes('ph') || label.includes('पीएच') || label.includes('పీహెచ్')) ph = val;
          else if (label.includes('rainfall') || label.includes('वर्षा') || label.includes('వర్షపాతం')) rain = val;
        });

        // Extract farming care guide
        const careContainer = document.querySelector('.info-cards-grid')?.parentElement?.querySelector('div.mt-4 p.text-light');
        const careText = careContainer ? careContainer.textContent.trim() : '';

        // Extract alternatives if present
        const altBadges = document.querySelectorAll('.glass-panel .badge.bg-dark');
        const alts = Array.from(altBadges).map(b => b.textContent.trim()).filter(Boolean);

        // Build continuous narrative according to language
        if (lang === 'te' || lang.startsWith('te')) {
          let s = `మీరు అందించిన వివరాల ఆధారంగా, సిఫార్సు చేయబడిన పంట ${cropName}`;
          if (confidence) s += `, దీని ఖచ్చితత్వం ${confidence} శాతం`;
          s += `. `;
          if (season && soil) s += `ఇది ${season} కాలంలో మరియు ${soil} నేలలో పండించడానికి ఎంతో అనుకూలం. `;
          else if (season) s += `ఇది ${season} కాలానికి అనుకూలం. `;
          else if (soil) s += `ఇది ${soil} నేలలో మంచి దిగుబడిని ఇస్తుంది. `;

          const conds = [];
          if (temp) conds.push(`ఉష్ణోగ్రత ${temp}`);
          if (hum) conds.push(`తేమ ${hum}`);
          if (ph) conds.push(`నేల పీహెచ్ ${ph}`);
          if (rain) conds.push(`వర్షపాతం ${rain}`);
          if (conds.length) s += `దీనికి కావలసిన అనుకూల పరిస్థితులు: ${conds.join(', ')}. `;

          if (careText) s += `సాగు మరియు సంరక్షణ సూచనలు: ${careText}. `;
          if (alts.length) s += `ఇతర ప్రత్యామ్నాయ పంటలు: ${alts.join(', ')}.`;
          return this.cleanTextForSpeech(s, lang);
        } else if (lang === 'hi' || lang.startsWith('hi')) {
          let s = `आपके द्वारा दी गई जानकारी के अनुसार, अनुशंसित फसल ${cropName} है`;
          if (confidence) s += `, जिसका विश्वास स्तर ${confidence} प्रतिशत है`;
          s += `। `;
          if (season && soil) s += `यह ${season} मौसम और ${soil} मिट्टी के लिए सबसे उपयुक्त है। `;
          else if (season) s += `यह ${season} मौसम के लिए उपयुक्त है। `;
          else if (soil) s += `यह ${soil} मिट्टी में सबसे अच्छी होती है। `;

          const conds = [];
          if (temp) conds.push(`तापमान ${temp}`);
          if (hum) conds.push(`आर्द्रता ${hum}`);
          if (ph) conds.push(`मिट्टी का पीएच ${ph}`);
          if (rain) conds.push(`वर्षा ${rain}`);
          if (conds.length) s += `इसके लिए आदर्श स्थितियों में ${conds.join(', ')} शामिल हैं। `;

          if (careText) s += `खेती के लिए उपयोगी सुझाव: ${careText}। `;
          if (alts.length) s += `इसके अलावा उपयुक्त विकल्प हैं: ${alts.join(', ')}।`;
          return this.cleanTextForSpeech(s, lang);
        } else {
          let s = `Based on the agricultural parameters you provided, ${cropName} is the recommended crop`;
          if (confidence) s += ` with a confidence of ${confidence} percent`;
          s += `. `;
          if (season && soil) s += `It is best cultivated during the ${season} season in ${soil} soil. `;
          else if (season) s += `It is best cultivated during the ${season} season. `;
          else if (soil) s += `It performs best in ${soil} soil. `;

          const conds = [];
          if (temp) conds.push(`optimal temperature of ${temp}`);
          if (hum) conds.push(`humidity around ${hum}`);
          if (ph) conds.push(`soil pH of ${ph}`);
          if (rain) conds.push(`annual rainfall of ${rain}`);
          if (conds.length) s += `Ideal growing conditions include ${conds.join(', ')}. `;

          if (careText) s += `Here are some useful farming suggestions: ${careText}. `;
          if (alts.length) s += `Other viable alternatives include ${alts.join(', ')}.`;
          return this.cleanTextForSpeech(s, lang);
        }
      }

      // ── B. Check for Leaf Disease Detection Result on Page ──
      const statusBanner = document.querySelector('.status-banner');
      const diseaseHeader = document.querySelector('.glass-panel h2.display-6');

      if (statusBanner && diseaseHeader) {
        const isHealthy = statusBanner.classList.contains('healthy') ||
                          statusBanner.textContent.toLowerCase().includes('healthy') ||
                          statusBanner.textContent.includes('स्वस्थ') ||
                          statusBanner.textContent.includes('ఆరోగ్యకరమైన');

        const diseaseName = diseaseHeader.textContent.trim();

        // Extract confidence
        const confBadge = document.querySelector('.confidence-bar-wrapper')?.previousElementSibling?.querySelector('.fw-bold');
        const confidence = confBadge ? confBadge.textContent.replace('%', '').trim() : '';

        // Extract pathology sections
        let cause = '', symptoms = '', solution = '', organic = '', prevention = '';
        const infoCards = document.querySelectorAll('.glass-panel .row.g-3 .info-card');

        infoCards.forEach(card => {
          const label = (card.querySelector('.info-card-label')?.textContent || '').toLowerCase();
          const p = card.querySelector('p')?.textContent?.trim() || '';
          if (label.includes('cause') || label.includes('कारण') || label.includes('కారణం')) cause = p;
          else if (label.includes('symptom') || label.includes('लक्षण') || label.includes('లక్షణాలు')) symptoms = p;
          else if (label.includes('treatment') || label.includes('उपचार') || label.includes('చికిత్స')) solution = p;
          else if (label.includes('organic') || label.includes('जैविक') || label.includes('సేంద్రీయ')) organic = p;
          else if (label.includes('prevention') || label.includes('रोकथाम') || label.includes('నివారణ')) prevention = p;
        });

        // Build continuous narrative according to language
        if (lang === 'te' || lang.startsWith('te')) {
          if (isHealthy) {
            return this.cleanTextForSpeech(
              `శుభవార్త! మీరు స్కాన్ చేసిన ఆకు ${confidence ? confidence + ' శాతం ఖచ్చితత్వంతో ' : ''}పూర్తిగా ఆరోగ్యంగా ఉంది. మొక్కలో ఎటువంటి వ్యాధి లక్షణాలు లేవు. పంటను ఆరోగ్యంగా ఉంచడానికి సరైన నీటి యాజమాన్యం మరియు ఎరువులను కొనసాగించండి.`,
              lang
            );
          }
          let s = `ఆకు స్కాన్ విశ్లేషణ ప్రకారం, గుర్తించబడిన సమస్య ${diseaseName}`;
          if (confidence) s += `, దీని ఖచ్చితత్వం ${confidence} శాతం`;
          s += `. `;
          if (cause) s += `దీనికి ముఖ్య కారణం: ${cause}. `;
          if (symptoms) s += `కనిపించే ప్రధాన లక్షణాలు: ${symptoms}. `;
          if (solution) s += `నివారణకు సిఫార్సు చేసిన చికిత్స: ${solution}. `;
          if (organic) s += `సేంద్రీయ నివారణ చర్యలు: ${organic}. `;
          if (prevention) s += `భవిష్యత్తులో వ్యాధి రాకుండా జాగ్రత్తలు: ${prevention}.`;
          return this.cleanTextForSpeech(s, lang);
        } else if (lang === 'hi' || lang.startsWith('hi')) {
          if (isHealthy) {
            return this.cleanTextForSpeech(
              `खुशखबरी! आपकी स्कैन की गई पत्ती ${confidence ? confidence + ' प्रतिशत विश्वास के साथ ' : ''}पूरी तरह स्वस्थ पाई गई है। पौधा रोगमुक्त है। फसल को स्वस्थ रखने के लिए नियमित निगरानी और संतुलित खाद जारी रखें।`,
              lang
            );
          }
          let s = `पत्ती की जांच के अनुसार, पहचानी गई बीमारी ${diseaseName} है`;
          if (confidence) s += `, जिसका विश्वास स्तर ${confidence} प्रतिशत है`;
          s += `। `;
          if (cause) s += `इसका मुख्य कारण है: ${cause}। `;
          if (symptoms) s += `दिखने वाले मुख्य लक्षण: ${symptoms}। `;
          if (solution) s += `उपचार के लिए रासायनिक समाधान: ${solution}। `;
          if (organic) s += `जैविक और प्राकृतिक उपाय: ${organic}। `;
          if (prevention) s += `भविष्य में रोकथाम के उपाय: ${prevention}।`;
          return this.cleanTextForSpeech(s, lang);
        } else {
          if (isHealthy) {
            return this.cleanTextForSpeech(
              `Great news! Your scanned leaf appears healthy with a confidence of ${confidence || 'high'} percent. The plant shows no visible signs of pathogen infection. Continue standard irrigation, adequate sunlight, and balanced nutrition to keep your crop healthy.`,
              lang
            );
          }
          let s = `Based on the leaf scan analysis, the detected condition is ${diseaseName}`;
          if (confidence) s += ` with a confidence of ${confidence} percent`;
          s += `. `;
          if (cause) s += `The primary biological cause is: ${cause}. `;
          if (symptoms) s += `Key visible symptoms include: ${symptoms}. `;
          if (solution) s += `Recommended chemical treatment: ${solution}. `;
          if (organic) s += `For eco-friendly organic management: ${organic}. `;
          if (prevention) s += `To prevent future occurrences: ${prevention}.`;
          return this.cleanTextForSpeech(s, lang);
        }
      }

      // ── C. Fallback for History Items or Individual Sub-buttons ──
      return this.cleanTextForSpeech(fallbackRawText, lang);
    }

    /**
     * Speaks the complete advisory text continuously as ONE SpeechSynthesisUtterance.
     */
    speak(textOrRaw, langCode = null, buttonEl = null) {
      if (!this.synth) {
        alert("Speech synthesis is not supported on this browser.");
        return;
      }

      const lang = (langCode || getActiveLanguage()).toLowerCase().trim();

      // Toggle behavior: If already speaking this button, stop it
      if (this.isPlaying && this.activeButton === buttonEl) {
        this.stop();
        return;
      }

      // 1. Cancel any active speech prior to starting new speech (Requirement 8)
      this.synth.cancel();
      this.isPlaying = false;

      // 2. Select appropriate voice with strict language enforcement
      const voice = this.getVoiceForLanguage(lang);

      // 3. Clear detection & reporting if Telugu or Hindi voice is missing (Requirement 3 & 9)
      if (lang === 'te' || lang.startsWith('te')) {
        if (!voice) {
          const teMsg = "Telugu voice (te-IN) is not installed on this device. Please install the Telugu voice package in your operating system or browser settings.";
          console.warn("[AgriAudioEngine] " + teMsg);
          this.showNotice("⚠️ " + teMsg, 6000);
          return;
        }
      } else if (lang === 'hi' || lang.startsWith('hi')) {
        if (!voice) {
          const hiMsg = "Hindi voice (hi-IN) is not installed on this device. Please install the Hindi voice package in system settings.";
          console.warn("[AgriAudioEngine] " + hiMsg);
          this.showNotice("⚠️ " + hiMsg, 6000);
          return;
        }
      }

      // 4. Build complete, conversational narrative
      const rawText = typeof textOrRaw === 'string' ? textOrRaw : (buttonEl?.getAttribute('data-speak') || buttonEl?.innerText || '');
      const conversationalText = this.buildConversationalSpeech(buttonEl, rawText, lang);

      if (!conversationalText) return;

      this.lastSpokenText = conversationalText;
      this.lastSpokenLang = lang;
      this.activeButton = buttonEl;

      // 5. Create ONE SpeechSynthesisUtterance for continuous natural playback (Requirement 4)
      const utterance = new SpeechSynthesisUtterance(conversationalText);

      if (voice) {
        utterance.voice = voice;
      }

      // 6. Explicit Language Tags (Requirement 1)
      if (lang === 'te' || lang.startsWith('te')) {
        utterance.lang = 'te-IN';
        utterance.rate = 0.90; // Requirement 7: Telugu rate 0.90
      } else if (lang === 'hi' || lang.startsWith('hi')) {
        utterance.lang = 'hi-IN';
        utterance.rate = 0.90; // Requirement 7: Hindi rate 0.90
      } else {
        utterance.lang = 'en-IN';
        utterance.rate = 0.92; // Requirement 7: English rate 0.92
      }
      utterance.pitch = 1.0; // Requirement 7: pitch 1.0

      utterance.onstart = () => {
        this.isPlaying = true;
        if (this.activeButton) {
          this.activeButton.classList.add('is-playing');
          const icon = this.activeButton.querySelector('.audio-icon');
          if (icon) icon.textContent = '⏹️';
        }
        this.showFloatingBar(conversationalText);
      };

      utterance.onend = () => {
        this.handlePlaybackEnd();
      };

      utterance.onerror = (e) => {
        console.warn("[AgriAudioEngine] Playback notice:", e);
        this.handlePlaybackEnd();
      };

      this.currentUtterance = utterance;

      // Start unified speech
      this.synth.speak(utterance);
    }

    stop() {
      if (this.synth) {
        this.synth.cancel();
      }
      this.handlePlaybackEnd();
    }

    replay() {
      if (this.lastSpokenText) {
        this.speak(this.lastSpokenText, this.lastSpokenLang, this.activeButton);
      }
    }

    handlePlaybackEnd() {
      this.isPlaying = false;
      if (this.activeButton) {
        this.activeButton.classList.remove('is-playing');
        const icon = this.activeButton.querySelector('.audio-icon');
        if (icon) icon.textContent = '🔊';
        this.activeButton = null;
      }
      this.hideFloatingBar();
    }

    createFloatingAudioBar() {
      if (document.getElementById('agriFloatingAudioBar')) return;

      const bar = document.createElement('div');
      bar.id = 'agriFloatingAudioBar';
      bar.style.cssText = `
        position: fixed;
        bottom: 24px;
        right: 24px;
        background: #092115;
        border: 1px solid #34d399;
        border-radius: 999px;
        padding: 8px 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        display: none;
        align-items: center;
        gap: 12px;
        z-index: 9999;
        color: #f0fdf4;
        font-size: 0.88rem;
        backdrop-filter: blur(10px);
        max-width: 440px;
        transition: all 0.25s ease-in-out;
      `;
      bar.innerHTML = `
        <span style="display:inline-flex;align-items:center;gap:8px;overflow:hidden;">
          <span id="audioStatusIcon" style="animation: pulse 1s infinite; font-size:1.1rem;">🔊</span>
          <span id="audioPlayingText" style="max-width:260px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:500;">Speaking advisory...</span>
        </span>
        <button id="audioReplayBtn" title="Replay" style="background:#059669;border:none;color:white;border-radius:50%;width:28px;height:28px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:0.8rem;">🔁</button>
        <button id="audioStopBtn" title="Stop" style="background:#f43f5e;border:none;color:white;border-radius:50%;width:28px;height:28px;cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:0.75rem;">⏹</button>
      `;
      document.body.appendChild(bar);

      const stopBtn = document.getElementById('audioStopBtn');
      if (stopBtn) {
        stopBtn.addEventListener('click', () => this.stop());
      }

      const replayBtn = document.getElementById('audioReplayBtn');
      if (replayBtn) {
        replayBtn.addEventListener('click', () => this.replay());
      }
    }

    showFloatingBar(text) {
      if (this.noticeTimer) {
        clearTimeout(this.noticeTimer);
        this.noticeTimer = null;
      }
      const bar = document.getElementById('agriFloatingAudioBar');
      const label = document.getElementById('audioPlayingText');
      const icon = document.getElementById('audioStatusIcon');
      if (bar && label) {
        bar.style.borderColor = '#34d399';
        if (icon) icon.textContent = '🔊';
        label.textContent = text;
        bar.style.display = 'flex';
      }
    }

    showNotice(message, durationMs = 5000) {
      const bar = document.getElementById('agriFloatingAudioBar');
      const label = document.getElementById('audioPlayingText');
      const icon = document.getElementById('audioStatusIcon');
      if (bar && label) {
        bar.style.borderColor = '#f59e0b';
        if (icon) icon.textContent = '⚠️';
        label.textContent = message;
        bar.style.display = 'flex';

        if (this.noticeTimer) clearTimeout(this.noticeTimer);
        this.noticeTimer = setTimeout(() => {
          this.hideFloatingBar();
        }, durationMs);
      }
    }

    hideFloatingBar() {
      const bar = document.getElementById('agriFloatingAudioBar');
      if (bar) bar.style.display = 'none';
    }
  }

  // Instantiate global audio
  window.agriAudio = new AgriAudioEngine();

  // Attach global listener for any button with data-speak attribute
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('[data-speak]');
    if (btn) {
      e.preventDefault();
      const textToSpeak = btn.getAttribute('data-speak') || btn.innerText;
      window.agriAudio.speak(textToSpeak, getActiveLanguage(), btn);
    }
  });


  // ── 2. Drag-and-Drop Image Upload Component ────────────────────────────
  function initDropzone() {
    const dropzone = document.getElementById('leafDropzone');
    const fileInput = document.getElementById('leafFileInput');
    const previewContainer = document.getElementById('previewContainer');
    const previewImg = document.getElementById('previewImg');
    const previewName = document.getElementById('previewName');
    const previewSize = document.getElementById('previewSize');
    const clearBtn = document.getElementById('clearImageBtn');
    const form = document.getElementById('diseaseUploadForm');
    const submitBtn = document.getElementById('submitScanBtn');
    const scanAnimation = document.getElementById('scanAnimation');

    if (!dropzone || !fileInput) return;

    function handleFile(file) {
      if (!file) return;

      // Validate file extension
      const validTypes = ['image/jpeg', 'image/png', 'image/webp', 'image/jpg'];
      if (!validTypes.includes(file.type)) {
        alert("Please upload a valid image file (PNG, JPG, JPEG, WEBP).");
        return;
      }

      // Validate size (5MB max)
      const maxSize = 5 * 1024 * 1024;
      if (file.size > maxSize) {
        alert("File size exceeds 5MB limit. Please upload a smaller image.");
        return;
      }

      const reader = new FileReader();
      reader.onload = (e) => {
        if (previewImg) previewImg.src = e.target.result;
        if (previewName) previewName.textContent = file.name;
        if (previewSize) previewSize.textContent = `${(file.size / 1024).toFixed(1)} KB`;
        if (previewContainer) previewContainer.style.display = 'block';
        dropzone.style.display = 'none';
        if (submitBtn) submitBtn.disabled = false;
      };
      reader.readAsDataURL(file);
    }

    dropzone.addEventListener('click', () => fileInput.click());

    fileInput.addEventListener('change', (e) => {
      if (e.target.files && e.target.files[0]) {
        handleFile(e.target.files[0]);
      }
    });

    ['dragenter', 'dragover'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.add('is-dragover');
      });
    });

    ['dragleave', 'drop'].forEach(eventName => {
      dropzone.addEventListener(eventName, (e) => {
        e.preventDefault();
        e.stopPropagation();
        dropzone.classList.remove('is-dragover');
      });
    });

    dropzone.addEventListener('drop', (e) => {
      const dt = e.dataTransfer;
      if (dt.files && dt.files[0]) {
        fileInput.files = dt.files;
        handleFile(dt.files[0]);
      }
    });

    if (clearBtn) {
      clearBtn.addEventListener('click', (e) => {
        e.preventDefault();
        fileInput.value = '';
        if (previewImg) previewImg.src = '';
        if (previewContainer) previewContainer.style.display = 'none';
        dropzone.style.display = 'block';
        if (submitBtn) submitBtn.disabled = true;
      });
    }

    if (form) {
      form.addEventListener('submit', () => {
        if (scanAnimation) scanAnimation.style.display = 'block';
        if (submitBtn) {
          submitBtn.disabled = true;
          submitBtn.innerHTML = `<span>⏳ Analyzing Leaf...</span>`;
        }
      });
    }
  }


  // ── 3. Quick-Test Agronomic Presets for Crop Form ──────────────────────
  function initCropPresets() {
    const presetButtons = document.querySelectorAll('[data-crop-preset]');
    if (!presetButtons.length) return;

    const PRESETS = {
      'rice': { N: 80, P: 40, K: 40, temperature: 24.5, humidity: 82.0, ph: 6.5, rainfall: 200.0 },
      'maize': { N: 80, P: 45, K: 20, temperature: 23.0, humidity: 65.0, ph: 6.5, rainfall: 70.0 },
      'chickpea': { N: 40, P: 60, K: 80, temperature: 18.0, humidity: 16.0, ph: 7.0, rainfall: 80.0 },
      'cotton': { N: 120, P: 45, K: 20, temperature: 24.0, humidity: 80.0, ph: 6.8, rainfall: 80.0 },
      'coffee': { N: 100, P: 30, K: 30, temperature: 26.0, humidity: 58.0, ph: 6.8, rainfall: 160.0 },
      'apple': { N: 20, P: 135, K: 200, temperature: 22.0, humidity: 92.0, ph: 5.9, rainfall: 110.0 }
    };

    presetButtons.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        const cropKey = btn.getAttribute('data-crop-preset');
        const vals = PRESETS[cropKey];
        if (!vals) return;

        for (const [key, value] of Object.entries(vals)) {
          const input = document.querySelector(`input[name="${key}"]`);
          if (input) {
            input.value = value;
            input.dispatchEvent(new Event('input', { bubbles: true }));
          }
        }

        // Highlight selected chip
        presetButtons.forEach(b => b.style.borderColor = 'rgba(52, 211, 153, 0.2)');
        btn.style.borderColor = '#34d399';
      });
    });
  }

  // ── Initialize on DOM Load ──
  document.addEventListener('DOMContentLoaded', () => {
    initDropzone();
    initCropPresets();
  });

})();
