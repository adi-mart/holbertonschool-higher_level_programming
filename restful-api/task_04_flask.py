#!/usr/bin/env python3
"""
Task 4: Develop a Simple API using Python with Flask
This module creates a Flask API with multiple endpoints for user management.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route("/")
def home():
    """
    Root endpoint that returns a welcome message.

    Returns:
        str: Welcome message
    """
    return ("Welcome to the Flask API")


@app.route("/data")
def get_data():
    """
    Data endpoint that returns a list of all usernames.

    Returns:
        JSON: List of usernames stored in the API
    """
    return (jsonify(list(users.keys())))


@app.route("/status")
def get_status():
    """
    Status endpoint that returns the API status.

    Returns:
        str: Status message "OK"
    """
    return ("OK")


@app.route("/users/<username>")
def get_user(username):
    """
    Get user endpoint that returns user data for a specific username.

    Args:
        username (str): Username to retrieve

    Returns:
        JSON: User data or error message
    """
    user = users.get(username)
    if user:
        return (jsonify(user))
    else:
        return (jsonify({"error": "User not found"}))


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
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get("username")
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    return (jsonify({"message": "User added", "user": users[username]})), 201


if __name__ == "__main__":
    app.run()
