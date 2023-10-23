#!/usr/bin/python3
"""returns employee's TODO list progress"""
import json
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_res = requests.get("{}/users/{}".format(url, id)).json()
    todos_res = requests.get("{}/todos".
                             format(url), params={"userId": id}).json()
    username = user_res.get("username")
    with open("{}.json".format(id), "w") as file:
        rows = []
        for i in todos_res:
            rows += [{"task": i.get("title"),
                      "completed": i.get("completed"),
                      "username": username}]
        json.dump({id: rows}, file)
