#!/usr/bin/python3
"""
extending the Python script to export
data in the JSON format
"""


if __name__ == '__main__':
    import json
    import requests

    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url)
    users = response.json()
    url = "https://jsonplaceholder.typicode.com/todos/"
    response = requests.get(url)
    todos = response.json()
    data = {}
    for user in users:
        data[user.get("id")] = []
        for todo in todos:
            if todo.get("userId") == user.get("id"):
                data[user.get("id")].append({
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": user.get("username")
                })

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)
