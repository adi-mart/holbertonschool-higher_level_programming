#!/usr/bin/env python3
"""
Task 3: Develop a simple API using Python with the http.server module
This module creates a basic HTTP server with multiple endpoints.
"""

import http.server
import socketserver
import json


class APIRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom request handler for the simple API server.
    Handles GET requests for different endpoints.
    """
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints:
        - / : Returns a welcome message
        - /data : Returns sample JSON data
        - /status : Returns API status
        - Other paths : Returns 404 error
        """
        # TODO: Implement routing logic
        # - Check self.path to determine which endpoint was requested
        # - For "/" endpoint: return "Hello, this is a simple API!"
        # - For "/data" endpoint: return JSON data {"name": "John", "age": 30, "city": "New York"}
        # - For "/status" endpoint: return "OK"
        # - For any other path: return 404 Not Found
        # - Set appropriate headers (Content-Type, etc.)
        pass


def run_server(port=8000):
    """
    Start the HTTP server on the specified port.
    
    Args:
        port (int): Port number to run the server on (default: 8000)
    """
    # TODO: Implement server startup
    # - Create server instance using socketserver.TCPServer
    # - Use APIRequestHandler as the request handler
    # - Start the server and handle requests
    pass


if __name__ == "__main__":
    # TODO: Call run_server() to start the server
    print("Starting server on http://localhost:8000")
    # run_server()
    pass