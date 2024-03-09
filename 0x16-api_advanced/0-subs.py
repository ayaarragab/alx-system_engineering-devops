#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and returns the
"""
import requests


def number_of_subscribers(subreddit):
    """
    return number_of_subscribers
    """
    headers = {'User-agent': ''.join(['Mozilla/5.0',
                                      '(Windows NT 10.0; Win64; x64)',
                                      'AppleWebKit/537.36 (KHTML, like Gecko)',
                                      'Chrome/58.0.3029.110',
                                      'Safari/537.3'])}
    url = 'https://www.reddit.com/r/{}/about/.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0


number_of_subscribers('programming')
