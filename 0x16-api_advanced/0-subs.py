#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns the
"""
import requests


def number_of_subscribers(subreddit):
    """
    return number_of_subscribers
    """
    headers = {'User-Agent': "My-User-Agent"}

    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
