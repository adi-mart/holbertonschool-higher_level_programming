#!/usr/bin/env python3
"""
Task 4: Develop a Simple API using Python with Flask
This module creates a Flask API with multiple endpoints for user management.
"""

from flask import Flask, jsonify, request

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for users
# Example: users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}
users = {}


@app.route("/")
def home():
    """
    Root endpoint that returns a welcome message.
    
    Returns:
        str: Welcome message
    """
    # TODO: Return "Welcome to the Flask API!"
    pass


@app.route("/data")
def get_data():
    """
    Data endpoint that returns a list of all usernames.
    
    Returns:
        JSON: List of usernames stored in the API
    """
    # TODO: Return a JSON list of all usernames from the users dictionary
    # Example: ["jane", "john"] if those users exist
    pass


@app.route("/status")
def get_status():
    """
    Status endpoint that returns the API status.
    
    Returns:
        str: Status message "OK"
    """
    # TODO: Return "OK"
    pass


@app.route("/users/<username>")
def get_user(username):
    """
    Get user endpoint that returns user data for a specific username.
    
    Args:
        username (str): Username to retrieve
        
    Returns:
        JSON: User data or error message
    """
    # TODO: Check if user exists in users dictionary
    # If exists: return the user data as JSON
    # If not exists: return {"error": "User not found"}
    pass


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Add user endpoint that accepts POST requests to add new users.
    
    Expected JSON payload:
    {
        "username": "john",
        "name": "John", 
        "age": 30,
        "city": "New York"
    }
    
    Returns:
        JSON: Success message with user data or error message
    """
    # TODO: 
    # 1. Get JSON data from request
    # 2. Check if "username" is provided - if not, return 400 error with {"error": "Username is required"}
    # 3. Add user to users dictionary using username as key
    # 4. Return 201 status with success message and user data:
    #    {"message": "User added", "user": {...user_data...}}
    pass


if __name__ == "__main__":
    # TODO: Run the Flask application
    # app.run()
    pass