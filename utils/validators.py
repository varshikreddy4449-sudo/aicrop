"""
utils/validators.py
Input validation helpers.
"""
import re


def validate_email(email: str) -> bool:
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))


def validate_username(username: str) -> bool:
    return bool(re.match(r"^[a-zA-Z0-9_]{3,30}$", username))


def validate_password(password: str) -> bool:
    return len(password) >= 6


def allowed_file(filename: str, allowed_extensions: set) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in allowed_extensions


def validate_crop_inputs(data: dict):
    """
    Validates and parses the 7 crop input fields.
    Returns (True, parsed_dict) on success or (False, error_message) on failure.
    """
    FIELDS = {
        "N":           (0,   140),
        "P":           (5,   145),
        "K":           (5,   205),
        "temperature": (8.0,  44.0),
        "humidity":    (14.0, 100.0),
        "ph":          (3.5,  10.0),
        "rainfall":    (20.0, 300.0),
    }

    parsed = {}
    for field, (low, high) in FIELDS.items():
        raw = data.get(field, "").strip() if isinstance(data.get(field), str) else str(data.get(field, ""))
        if raw == "" or raw == "None":
            return False, f"'{field}' is required."
        try:
            value = float(raw)
        except ValueError:
            return False, f"'{field}' must be a number."
        if not (low <= value <= high):
            return False, f"'{field}' must be between {low} and {high}."
        parsed[field] = value

    return True, parsed
# Aliases for backward compatibility with auth_routes.py
is_valid_email    = validate_email
is_valid_username = validate_username
is_valid_password = validate_password

# Alias for disease_routes.py
is_allowed_file   = allowed_file