#!/usr/bin/python3

"""Returns to-do list information for a given employee ID.

This script retrieves the to-do list information for a specific employee
from a REST API and displays the completed tasks.

Usage:
    $ python3 to_do_list.py <employee_id>

Arguments:
    employee_id (int): The ID of the employee to retrieve the to-do list for.

"""

import sys
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"

    # Retrieve user information
    user = requests.get(URL + f"users/{sys.argv[1]}", timeout=20).json()

    # Retrieve to-do list
    todos = requests.get(URL + "todos", params={"userId": sys.argv[1]}, timeout=20).json()

    # Filter completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Display results
    print(f"Employee {user.get('name')} is done with tasks ({len(completed)}/{len(todos)}):")
    for i in completed:
        print(f"\t {i}")
