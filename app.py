from flask import Flask, render_template, url_for, redirect, request, flash
import numpy as np
import sys
import datetime
import json
import requests
import fire
import path

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/isfire', methods=['POST'])
def isfire():
    arr = [0]
    source_node = request.form['source_node']
    flag = False
    for i in range(6):
        file = request.files[str(i+1)]
        res = fire.fire("images/" + file.filename)
        arr.append(res)
        flag = res

    if not flag:
        return "You are safe!"

    final_path = path.path(arr, source_node)

    return render_template('index.html', path=final_path)


if __name__=="__main__":
    app.run(port=5000, debug=True)