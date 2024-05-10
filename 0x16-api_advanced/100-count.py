#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""


def count_words(subreddit, word_list, word_counts=None, after=None):
    import requests

    word_list = list(dict.fromkeys(word_list))

    if word_counts is None:
        word_counts = {word.lower(): 0 for word in word_list}

    headers = {'User-Agent': "My-User-Agent"}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params={
            'after': after})

    if response.status_code != 200:
        return

    data = response.json()
    articles = data['data']['children']
    titles = [article['data']['title'] for article in articles]
    for title in titles:
        for word in word_list:
            splitted = title.lower().split()
            for title__ in splitted:
                if word.lower() == title__:
                    word_counts[word] += 1

    if data.get('data').get('after'):
        count_words(
            subreddit,
            word_list,
            word_counts,
            data.get('data').get('after'))

    if after is None:
        sorted_counts = sorted(word_counts.items(), key=lambda kv: kv[0])
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
