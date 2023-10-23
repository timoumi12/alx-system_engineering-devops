#!/usr/bin/python3
"""returns employee's TODO list progress"""
import csv
import requests
import sys


if __name__ == "__main__":
    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user_res = requests.get("{}/users/{}".format(url, id)).json()
    todos_res = requests.get("{}/todos".
                             format(url), params={"userId": id}).json()
    with open("{}.csv".format(id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for i in todos_res:
            row = [i.get("userId"),
                user_res.get("name"),
                i.get("completed"),
                i.get("title")]
            writer.writerow(row)
