#!/usr/bin/python3
"""Use REST API to get data andexport to csv file"""
import csv
import json
import requests
from sys import argv


def main():
    """main function"""
    if len(argv) < 2:
        return

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    user_request = requests.get(user_url)
    user = json.loads(user_request.text)
    todo_request = requests.get(todo_url)
    todo = json.loads(todo_request.text)

    with open("{}.csv".format(argv[1]), mode='w') as file:
        file = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            file.writerow([argv[1],
                           user.get('username'),
                           task.get('completed'),
                           task.get('title')])


if __name__ == "__main__":
    main()
