#!/usr/bin/python3
"""Use Reddit API to get data"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """function that return the first
    10 hot post a givven subreddit"""

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit, after)
    header = {"User-Agent": "ubuntu:test:v1.0 (by /u/kemitche)"}
    param = {'after': after}
    request = requests.get(url, headers=header, params=param)

    if request.status_code == 404:
        return(None)
    elif after is None:
        return
    else:
        for childs in request.json()["data"]["children"]:
                hot_list.append(childs["data"]["title"])
        after = request.json()["data"]["after"]
        recurse(subreddit, hot_list, after)
        return(hot_list)
