#!/usr/bin/python3
"""Use REST API to get data"""
from sys import argv
import requests
import json


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

    number_of_task = len(todo)
    number_task_complete = 0

    for task in todo:
        if task.get('completed'):
            number_task_complete += 1

    print("Employee {} is done with tasks({}/{})".format(user.get('name'),
                                                         number_task_complete,
                                                         number_of_task))

    for task in todo:
        if task.get('completed'):
            print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    main()
