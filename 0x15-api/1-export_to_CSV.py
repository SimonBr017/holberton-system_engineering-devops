#!/usr/bin/python3
from sys import argv
import requests
import json
import csv


def main():

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
                           user['name'],
                           task['completed'],
                           task['title']])


if __name__ == "__main__":
    main()
