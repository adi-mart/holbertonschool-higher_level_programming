#!/usr/bin/env python3
"""
Task 2: Consuming and processing data from an API using Python
This module provides functions to fetch and process data
from JSONPlaceholder API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder API and prints their titles.
    Also prints the status code of the response.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"(Status Code): {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for i in posts:
            print(i.get("title"))


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder API and saves them to a CSV file.
    Creates posts.csv with columns: id, title, body
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"(Status Code): {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', "w", newline="") as csvfile:
            writer = csv.DictWriter(
                csvfile, fieldnames=["id", "title", "body"])
            writer.writeheader()
            for i in posts:
                writer.writerow({
                    "id": i["id"],
                    "title": i["title"],
                    "body": i["body"]
                })
