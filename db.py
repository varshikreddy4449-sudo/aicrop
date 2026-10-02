"""
db.py
MongoDB connection setup using PyMongo.
Provides reusable collection objects for the whole app.
"""

import os
import logging
from pymongo import MongoClient, errors
from datetime import datetime
from config import Config

logger = logging.getLogger("AgriAI.DB")

MONGO_URI = getattr(Config, "MONGO_URI", os.environ.get("MONGO_URI", "mongodb://localhost:27017/"))
DB_NAME = getattr(Config, "DB_NAME", os.environ.get("DB_NAME", "AgriAI_DB"))

_client = None
_db = None
_is_connected = False

try:
    _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=2500)
    # Ping database to verify connection
    _client.admin.command('ping')
    _db = _client[DB_NAME]
    _is_connected = True
    logger.info("Successfully connected to MongoDB (%s, DB: %s)", MONGO_URI, DB_NAME)
except Exception as e:
    logger.warning("MongoDB connection warning: %s. App running with degraded DB persistence.", e)
    # Fallback client (will retry when requested)
    _client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=1000)
    _db = _client[DB_NAME]
    _is_connected = False

# Collections
users_collection = _db["users"]
crop_predictions_collection = _db["crop_predictions"]
disease_predictions_collection = _db["disease_predictions"]
disease_solutions_collection = _db["disease_solutions"]


def is_db_connected() -> bool:
    """Check if MongoDB is currently alive and responsive."""
    try:
        _client.admin.command('ping')
        return True
    except Exception:
        return False


def init_indexes():
    """Create indexes for performance and uniqueness constraints."""
    try:
        users_collection.create_index("email", unique=True)
        users_collection.create_index("username", unique=True)
        crop_predictions_collection.create_index("user_id")
        disease_predictions_collection.create_index("user_id")
        disease_solutions_collection.create_index("disease_name", unique=True)
        return True
    except Exception as e:
        logger.warning("Could not initialize MongoDB indexes: %s", e)
        return False


def get_server_time():
    return datetime.utcnow()
