#!/usr/bin/python3
"""
extending the Python script to export
data in the JSON format
"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv

    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    response = requests.get(url)
    user = response.json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
          user_id)
    response = requests.get(url)
    todos = response.json()
    data = {user_id: []}
    for todo in todos:
        data[user_id].append({
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")
        })
    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)
