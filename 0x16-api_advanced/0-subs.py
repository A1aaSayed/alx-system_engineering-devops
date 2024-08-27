#!/usr/bin/python3
"""function that queries the Reddit API"""

import requests


def number_of_subscribers(subreddit):
    """prints the number of subscribers for a given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {'User-Agent': 'python:subreddit.subscriber.count:v1.0 (by /u/Alaa)'}

    req = requests.get(url, headers=headers).json()
    subs = req.get('data', {}).get('subscribers', 0)

    return subs
