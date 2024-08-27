#!/usr/bin/python3
"""Module that queries the Reddit API"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
            'User-Agent': 'python:subreddit.top.ten:v1.0 (by /u/A1aaSayed)'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
