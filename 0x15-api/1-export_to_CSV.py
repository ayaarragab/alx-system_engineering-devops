#!/usr/bin/python3
"""
This script exports the data from the database to a CSV file.
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv
    if len(argv) > 1:
        user_Id = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        user_request = get("{}users/{}".format(url, user_Id))
        name = user_request.json().get('name')
        if name is not None:
            todo_request = get(
                "{}todos?userId={}".format(url, user_Id)).json()

        with open('{}.csv'.format(user_Id), 'w') as f:
            for task in todo_request:
                f.write('"{}","{}","{}","{}"\n'.format(
                    user_Id, name, task.get('completed'), task.get('title')))
