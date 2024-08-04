#!/usr/bin/python3
"""Module documented"""
import csv
import json
import requests
from sys import argv
"""Module documented"""


def main():
    """Moduel documented"""
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{user_id}"
    todos_url = f"{url}/todos?userId={user_id}"
    filename = f"{user_id}.csv"

    # Fetch user data
    resp1 = requests.get(user_url)
    resp1.raise_for_status()
    user_data = resp1.json()

    # Fetch todos data
    resp2 = requests.get(todos_url)
    resp2.raise_for_status()
    todos = resp2.json()

    data = []
    for task in todos:
        data.append([user_id, user_data["username"],
                     task["completed"], task["title"]])

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(data)


if __name__ == '__main__':
    """Module Docuemented"""
    main()
