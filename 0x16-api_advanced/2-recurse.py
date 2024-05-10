#!/usr/bin/python3
"""
a recursive function that queries the
Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
If no results are found for the given
subreddit, the function should return None.
"""


def recurse(subreddit, hot_list=[], after=None):
    """
    a recursive function that queries the
    Reddit API and returns a list containing the titles
    of all hot articles for a given subreddit.
    If no results are found for the given
    subreddit, the function should return None.
    """
    import requests

    headers = {'User-Agent': "My-User-Agent"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params={'after': after})

    if response.status_code != 200:
        return None

    data = response.json()
    articles = data['data']['children']
    titles = [article['data']['title'] for article in articles]
    hot_list.extend(titles)

    if data.get('data').get('after'):
        return recurse(subreddit, hot_list, data.get('data').get('after'))
    elif hot_list:
        return hot_list
    else:
        return None
