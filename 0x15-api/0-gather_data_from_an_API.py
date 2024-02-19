#!/usr/bin/python3
"""
python script gathers data from a rest API
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
        number_of_tasks = len(todo_request)
        completed_tasks = list()
        for task in todo_request:
            if task.get('completed') is True:
                completed_tasks.append(task)
        len_completed = len(completed_tasks)
        print("Employee {} is done with tasks({}/{}):".format(
              name, len_completed, number_of_tasks))
        for task in completed_tasks:
            print("\t {}".format(task.get('title')))
