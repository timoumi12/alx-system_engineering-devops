#!/usr/bin/python3
"""returns employee's TODO list progress"""
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_res = requests.get("{}/users/{}".format(url, id)).json()
    todos_res = requests.get("{}/todos".
                             format(url), params={"userId": id}).json()
    c_todos = []
    for i in todos_res:
        if i.get("completed") is True:
            c_todos.append(i)
    print("Employee {} is done with tasks({}/{}):"
          .format(user_res.get("name"), len(c_todos), len(todos_res)))
    for i in c_todos:
        print("\t {}".format(i.get("title")))
