#!/usr/bin/python3
"""Module documented"""
import json
import requests
"""Module documented"""


def main():
    """Moduel documented"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/"
    filename = "todo_all_employees.json"

    resp1 = requests.get(user_url)
    user_data = resp1.json()

    data = {}
    for user in user_data:
        user_id = user["id"]
        data[user_id] = []
        todos_url = f"{url}/todos?userId={user_id}"
        req = requests.get(todos_url)
        tasks = req.json()
        for task in tasks:
            data[user_id].append({
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            })
    with open(filename, 'w', newline='') as f:
        json.dump(data, f)


if __name__ == '__main__':
    """Module Docuemented"""
    main()
