#!/usr/bin/python3
""" Task 0 """
import json
import requests


def number_of_subscribers(subreddit):
    user = {"User-Agent": "Abdou-Hidoussi"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
