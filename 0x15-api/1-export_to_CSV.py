#!/usr/bin/python3

"""Exports to-do list information for a given employee ID to CSV format.

This script retrieves the to-do list information for a specific employee
from a REST API and exports it to a CSV file.

Usage:
    $ python3 export_to_csv.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee to retrieve the to-do list for.

"""

import sys
import csv
import requests

if __name__ == "__main__":
    # Retrieve user ID from command line arguments
    USER_ID = sys.argv[1]

    # API URL
    URL = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(URL + f"users/{USER_ID}", timeout=20).json()
    username = user.get("username")

    # Retrieve to-do list
    todos = requests.get(URL + "todos", params={"userId": USER_ID}, timeout=20).json()

    # Export to CSV file
    with open(f"{USER_ID}.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([USER_ID, username, todo.get("completed"), todo.get("title")])
