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
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['JWT_SECRET_KEY'] = 'your-secret-string'  # Change this secret key in production

# Initialize extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data with hashed passwords and roles
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


# Basic Authentication
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
    # TODO: Implement password verification
    # 1. Check if user exists in users dictionary
    # 2. Verify password using check_password_hash
    # 3. Return username if valid, None if invalid
    pass


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Protected route using basic authentication.
    
    Returns:
        str: Success message if authenticated
    """
    # TODO: Return "Basic Auth: Access Granted"
    pass


# JWT Authentication
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
    # TODO: Implement login logic
    # 1. Get JSON data from request
    # 2. Extract username and password
    # 3. Verify credentials against users dictionary
    # 4. If valid, create JWT token with user info (username, role)
    # 5. Return {"access_token": token} or error message
    pass


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Protected route using JWT authentication.
    
    Returns:
        str: Success message if authenticated with valid JWT
    """
    # TODO: Return "JWT Auth: Access Granted"
    pass


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Protected route that requires admin role.
    
    Returns:
        str or JSON: Success message if admin, error if not admin
    """
    # TODO: Implement admin role check
    # 1. Get current user identity from JWT token
    # 2. Check user's role in users dictionary
    # 3. If admin: return "Admin Access: Granted"
    # 4. If not admin: return 403 error with {"error": "Admin access required"}
    pass


# JWT Error Handlers
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
    # TODO: Run the Flask application
    # app.run(debug=True)
    pass