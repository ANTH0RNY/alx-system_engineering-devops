#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests

if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + f"users/{sys.arv[1]}", timeout=20).json()
    todos = requests.get(URL + "todos", params={"userId": sys.argv[1]}, timeout=20).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print(f"Employee {user.get('name')} is done with \
            tasks({len(completed)}/{len(todos)}):")
    for i in completed:
        print(f"\t {i}")
