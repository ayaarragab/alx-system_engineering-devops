#!/usr/bin/python3
"""
This script is used to retrieve and display the top ten
posts from a Reddit subreddit.
"""


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    import requests

    headers = {'User-Agent': "My-User-Agent"}

    url = 'https://www.reddit.com/r/{}/hot/.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get('children')
            if children:
                for child in children:
                    print(child.get('data').get('title'))
                return
    elif response.status_code >= 300:
        print('None')
