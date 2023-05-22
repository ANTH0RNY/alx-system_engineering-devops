#!/usr/bin/python3

"""
Exports to-do list information of all employees to JSON format.

This script retrieves the to-do list information for all employees
from a REST API and exports it to a JSON file.

"""

import json
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    users = requests.get(URL + "users", timeout=20).json()

    with open("todo_all_employees.json", "w", encoding='utf-8') as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(URL + "todos",
                                    params={"userId": u.get("id")}, timeout=20).json()]
            for u in users}, jsonfile)
