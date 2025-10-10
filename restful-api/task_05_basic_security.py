#!/usr/bin/env python3
"""
Task 5: API Security and Authentication Techniques
This module implements a Flask API with various authentication methods:
- Basic HTTP Authentication
- JWT (JSON Web Token) Authentication
- Role-based Access Control
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret key here'
auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for basic authentication.

    Args:
        username (str): Username
        password (str): Password

    Returns:
        str: Username if authentication successful, None otherwise
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Protected route using basic authentication.

    Returns:
        str: Success message if authenticated
    """
    return ("Basic Auth: Access Granted")


@app.route("/login", methods=["POST"])
def login():
    """
    Login endpoint that returns JWT token for valid credentials.

    Expected JSON payload:
    {
        "username": "user1",
        "password": "password"
    }

    Returns:
        JSON: Access token or error message
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if users and check_password_hash(user["password"], password):
        identity = {"username": username, "role": user["role"]}
        access_token = create_access_token(identity=identity)
        return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.

    Returns:
        str: Success message if authenticated with valid JWT
    """
    return ("JWT Auth: Access Granted")


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Protected route that requires admin role.

    Returns:
        str or JSON: Success message if admin, error if not admin
    """
    demande = get_jwt()
    if demande.get("role") == "admin":
        return ("Admin Access Granted")
    else:
        return (jsonify({"error": "Admin access required"})), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token errors."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle fresh token required errors."""
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
