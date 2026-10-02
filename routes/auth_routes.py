"""
routes/auth_routes.py
Handles user registration, login, and logout with resilient database access.
"""
import logging
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from bson.objectid import ObjectId
from db import users_collection, get_server_time, is_db_connected
from utils.auth_utils import hash_password, verify_password, login_required
from utils.validators import is_valid_email, is_valid_username, is_valid_password

logger = logging.getLogger("AgriAI.Auth")
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        errors = []
        if not is_valid_username(username):
            errors.append("Username must be 3-30 alphanumeric characters.")
        if not is_valid_email(email):
            errors.append("Please enter a valid email address.")
        if not is_valid_password(password):
            errors.append("Password must be at least 6 characters long.")
        if password != confirm_password:
            errors.append("Passwords do not match.")

        if errors:
            for err in errors:
                flash(err, "danger")
            return render_template("register.html", username=username, email=email)

        if not is_db_connected():
            flash("Database service is currently unreachable. Please ensure MongoDB is running.", "danger")
            return render_template("register.html", username=username, email=email)

        try:
            if users_collection.find_one({"$or": [{"email": email}, {"username": username}]}):
                flash("Username or email already registered.", "danger")
                return render_template("register.html", username=username, email=email)

            user_doc = {
                "username": username,
                "email": email,
                "password": hash_password(password),
                "created_at": get_server_time(),
            }
            users_collection.insert_one(user_doc)

            flash("Registration successful. Please log in with your credentials.", "success")
            return redirect(url_for("auth.login"))
        except Exception as e:
            logger.error("Registration error: %s", e)
            flash("Registration could not be completed. Please try again.", "danger")
            return render_template("register.html", username=username, email=email)

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip().lower()
        password = request.form.get("password", "")

        if not identifier or not password:
            flash("Please provide both username/email and password.", "danger")
            return render_template("login.html", identifier=identifier)

        if not is_db_connected():
            flash("Database service is currently unreachable. Please ensure MongoDB is running.", "danger")
            return render_template("login.html", identifier=identifier)

        try:
            user = users_collection.find_one({
                "$or": [{"email": identifier}, {"username": identifier}]
            })

            if not user or not verify_password(password, user["password"]):
                flash("Invalid credentials. Please verify your username/password.", "danger")
                return render_template("login.html", identifier=identifier)

            session["user_id"] = str(user["_id"])
            session["username"] = user["username"]

            flash(f"Welcome back, {user['username']}!", "success")
            return redirect(url_for("dashboard.dashboard"))
        except Exception as e:
            logger.error("Login error: %s", e)
            flash("Login attempt failed. Please check database connection.", "danger")
            return render_template("login.html", identifier=identifier)

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    session.clear()
    flash("You have been successfully logged out.", "info")
    return redirect(url_for("auth.login"))
