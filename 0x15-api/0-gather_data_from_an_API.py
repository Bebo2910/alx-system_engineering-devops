#!/usr/bin/python3
"""Module documented"""
import requests
import json
from sys import argv
"""Module documented"""


def main():
    """Moduel documented"""
    if len(argv) < 2:
        print("Usage: ./script_name.py <user_id>")
        return

    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{user_id}"
    todos_url = f"{url}/todos?userId={user_id}"

    # Fetch user data
    resp1 = requests.get(user_url)
    resp1.raise_for_status()
    user_data = resp1.json()

    # Fetch todos data
    resp2 = requests.get(todos_url)
    resp2.raise_for_status() 
    todos = resp2.json()

    tasks = [task['title'] for task in todos if task["completed"]]

    print(f"Employee {user_data.get('name')} is done with tasks({len(tasks)}/{len(todos)}):")
    for task in tasks:
        print(f"\t {task}")

if __name__ == '__main__':
    """Module Docuemented"""
    main()