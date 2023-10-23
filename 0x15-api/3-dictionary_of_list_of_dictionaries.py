#!/usr/bin/python3
"""returns employee's TODO list progress"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(url)).json()
    with open("todo_all_employees.json", "w") as file:
        res = {}
        for user in users:
            rows = []
            id = user.get("id")
            username = user.get("username")
            todos = requests.get("{}/todos".format(url),
                                 params={"userId": id}).json()
            for todo in todos:
                rows += [{"username": username,
                          "task": todo.get("title"),
                          "completed": todo.get("completed")}]
            res[id] = rows
        json.dump(res, file)
