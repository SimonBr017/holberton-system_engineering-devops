#!/usr/bin/python3
from sys import argv
import requests
import json


def main():

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
        if task['completed']:
            number_task_complete += 1

    print("Employee {} is done with tasks({}/{})".format(user['name'],
                                                         number_task_complete,
                                                         number_of_task))

    for task in todo:
        if task['completed']:
            print("\t {}".format(task['title']))


if __name__ == "__main__":
    main()
