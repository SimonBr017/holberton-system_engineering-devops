#!/usr/bin/python3
"""Use REST API to get data and export to json file"""
from sys import argv
import requests
import json


def main():
    """main function"""

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(argv[1])
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        argv[1])

    user_request = requests.get(user_url)
    user = json.loads(user_request.text)
    todo_request = requests.get(todo_url)
    todo = json.loads(todo_request.text)

    task_list = []
    todo_user = {}

    for task in todo:
        data = {"task": task['title'],
                "completed": task['completed'], "username": user['name']}
        task_list.append(data)
    todo_user[argv[1]] = task_list

    with open("{}.json".format(argv[1]), "w") as file:
        json.dump(todo_user, file)


if __name__ == "__main__":
    main()
