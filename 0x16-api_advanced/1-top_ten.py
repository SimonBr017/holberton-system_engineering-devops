#!/usr/bin/python3
"""Use Reddit API to get data"""
import requests


def top_ten(subreddit):
    """function that return the first
    10 hot post a givven subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {"User-Agent": "ubuntu:test:v1.0 (by /u/kemitche)"}

    request = requests.get(url, headers=header)

    if request.status_code == 404:
        return 0

    for child in request.json().get("data").get("children"):
        print(child.get("data").get("title"))