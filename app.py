# coding: utf-8

from flask import Flask

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup


@app.route('/')
def hello_world():
    req = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=뿌우")

    soup = BeautifulSoup(req.text, 'html.parser')

    print(soup)

    print("Test Get")




    return 'Hello World!'


if __name__ == '__main__':
    app.run('0.0.0.0', port=80)