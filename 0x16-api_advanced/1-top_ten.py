#!/usr/bin/python3
"""
This script is used to retrieve and display the top ten posts from a Reddit subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    headers = {'Accept': 'application/json',
               'User-Agent': ' '.join([
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
                   'AppleWebKit/537.36 (KHTML, like Gecko)',
                   'Chrome/97.0.4692.71',
                   'Safari/537.36',
                   'Edg/97.0.1072.62'
               ])}
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
    print('None')
