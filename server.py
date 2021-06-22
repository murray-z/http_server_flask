# -*- coding: utf-8 -*-


import json
from flask import Flask, request
from logger import generator_logging


logger = generator_logging("./log.txt")

app = Flask(__name__)


@app.route("/add", methods=["POST"])
def add():
    data = json.loads(request.data)
    try:
        a = data["a"]
        b = data["b"]
        c = a+b
        logger.info("Success")
        return json.dumps({"res": c, "msg": "success", "code": 1})
    except Exception as e:
        logger.info("Error: INFO: {} INPUT: {}".format(str(e), json.dumps(data)))
        return json.dumps({"res": "", "msg": str(e), "code": 0})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7777)