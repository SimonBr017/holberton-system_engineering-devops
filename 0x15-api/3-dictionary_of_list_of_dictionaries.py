#!/usr/bin/python3
from sys import argv
import requests
import json


def main():

    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user_request = requests.get(user_url)
    users = json.loads(user_request.text)
    todo_request = requests.get(todo_url)
    todo = json.loads(todo_request.text)

    todo_all_user = {}
    task_list = []

    for user in users:

        for task in todo:
            if task['userId'] == user['id']:
                data = {"username": user['name'],
                        "task": task['title'], "completed": task['completed']}
                task_list.append(data)

        todo_all_user[user['id']] = task_list

    with open("todo_all_employees.json", mode='w') as file:
        json.dump(todo_all_user, file)


if __name__ == "__main__":
    main()
