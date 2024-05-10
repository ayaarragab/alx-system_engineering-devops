#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""


def count_words(subreddit, word_list, index=0, word_counts=None):
    """
    a recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not).
    """
    import requests
    if word_counts is None:
        word_counts = {word.lower(): 0 for word in word_list}

    if index >= len(word_list):
        sorted_counts = {
            k: v for k,
            v in sorted(
                word_counts.items(),
                key=lambda item: item[1],
                reverse=True)}
        return sorted_counts

    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers)
    data = response.json()
    articles = data['data']['children']

    for article in articles:
        title = article['data']['title'].lower()
        if word_list[index].lower() in title:
            word_counts[word_list[index].lower()] += 1

    return count_words(subreddit, word_list, index + 1, word_counts)
