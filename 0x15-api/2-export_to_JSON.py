#!/usr/bin/python3

"""
Exports to-do list information for a given employee ID to JSON format.

This script retrieves the to-do list information for a specific employee
from a REST API and exports it to a JSON file.

Usage:
    $ python3 export_to_json.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee to retrieve the to-do list for.

"""

import sys
import json
import requests

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    URL = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(URL + f"users/{USER_ID}", timeout=20).json()
    username = user.get("username")

    # Retrieve to-do list
    todos = requests.get(URL + "todos", params={"userId": USER_ID}, timeout=20).json()

    # Export to JSON file
    with open(f"{USER_ID}.json", "w", encoding='utf-8') as jsonfile:
        json.dump({USER_ID: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
