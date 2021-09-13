#!/usr/bin/python3
"""Use REST API to get data and export to json file"""
import json
import requests
from sys import argv


def main():
    """main function"""

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user_request = requests.get(user_url)
    users = json.loads(user_request.text)
    todo_request = requests.get(todo_url)
    todo = json.loads(todo_request.text)

    todo_all_user = {}

    for user in users:
        task_list = []
        for task in todo:
            if task.get('userId') == user.get('id'):
                data = {"username": user.get('username'),
                        "task": task.get('title'),
                        "completed": task.get('completed')}
                task_list.append(data)
        todo_all_user[user.get('id')] = task_list

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(todo_all_user, file)


if __name__ == "__main__":
    main()
