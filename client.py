# -*- coding: utf-8 -*-

import json
import requests


def clinet():
    url = "http://localhost:7777/add"
    res = requests.post(url=url, data=json.dumps({"a": 1, "b": 3}))
    print(res.json())


if __name__ == "__main__":
    clinet()