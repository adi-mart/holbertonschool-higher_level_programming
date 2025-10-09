#!/usr/bin/env python3
"""
Task 3: Develop a simple API using Python with the http.server module
This module creates a basic HTTP server with multiple endpoints.
"""

import http.server
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
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())
        else:
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run_server(
    server_class=http.server.HTTPServer,
    handler_class=APIRequestHandler,
):
    """
    Start the HTTP server on the specified port.

    Args:
        port (int): Port number to run the server on (default: 8000)
    """
    # ...existing code...
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()
