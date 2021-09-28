#!/usr/bin/python3
"""Use Reddit API to get data"""
import requests


def number_of_subscribers(subreddit):
    """function that return the number of
    subscriber for a givven subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {"User-Agent": "ubuntu:test:v1.0 (by /u/kemitche)"}

    request = requests.get(url, headers=header)

    if request.status_code == 404:
        return 0

    return(request.json().get("data").get("subscribers"))
