#!/usr/bin/python3
"""
python script gathers data from a rest API
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
           argv[1])

    response = get(url)

    data = response.json()
    user = get('https://jsonplaceholder.typicode.com/users/{}'.format(
               argv[1])).json()
    completed = [task for task in data if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.format(
          user.get('name'), len(completed), len(data)))
    [print('\t{}'.format(task.get('title'))) for task in completed]
