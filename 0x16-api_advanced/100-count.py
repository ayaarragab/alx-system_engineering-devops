#!/usr/bin/python3
"""
a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).
"""


# def count_words(subreddit, word_list, word_counts=None, after=None):
#     """
#     a recursive function that queries the Reddit API, parses the title of all
#     hot articles, and prints a sorted count of given keywords
#     (case-insensitive, delimited by spaces. Javascript should count as
#     javascript, but java should not).
#     """
#     import requests

#     word_list = list(dict.fromkeys(word_list))

#     if word_counts is None:
#         word_counts = {word.lower(): 0 for word in word_list}

#     headers = {'User-Agent': "My-User-Agent"}
#     url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
#     response = requests.get(url, headers=headers, allow_redirects=False, params={'after': after})
#     data = response.json()
#     articles = data['data']['children']
#     titles = [article['data']['title'] for article in articles]
#     for title in titles:
#         for word in word_list:
#             if word.lower() in title.lower():
#                 word_counts[word] += 1
#     if data.get('data').get('after'):
#         count_words(subreddit, word_list, word_counts, data.get('data').get('after'))
#     else:
#         sorted_counts = sorted(word_counts.items(), key=lambda kv: kv[0])
#         [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]

#!/usr/bin/python3
"""Module for task 3"""


def count_words(subreddit, word_list, word_count={}, after=None):
    """Queries the Reddit API and returns the count of words in
    word_list in the titles of all the hot posts
    of the subreddit"""
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code != 200:
        return None

    info = sub_info.json()

    hot_l = [child.get("data").get("title")
             for child in info
             .get("data")
             .get("children")]
    if not hot_l:
        return None

    word_list = list(dict.fromkeys(word_list))

    if word_count == {}:
        word_count = {word: 0 for word in word_list}

    for title in hot_l:
        split_words = title.split(' ')
        for word in word_list:
            for s_word in split_words:
                if s_word.lower() == word.lower():
                    word_count[word] += 1

    if not info.get("data").get("after"):
        sorted_counts = sorted(word_count.items(), key=lambda kv: kv[0])
        sorted_counts = sorted(word_count.items(),
                               key=lambda kv: kv[1], reverse=True)
        [print('{}: {}'.format(k, v)) for k, v in sorted_counts if v != 0]
    else:
        return count_words(subreddit, word_list, word_count,
                           info.get("data").get("after"))
