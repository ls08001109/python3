#coding=utf-8

from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/')
def webTemplate():
    return render_template('atmovies.html')


@app.route('/handler', methods=['post'])
def handler():
    movies = request.form["movies"]
    os.chdir("crawler_demo")
    os.system("scrapy crawl atmovies -a moviesName=" + movies)
    os.chdir("..")
    return "OK"


@app.route('/read_csv', methods=['post'])
def read_csv():
    with open("/tmp/data.csv", "r", encoding='utf-8') as f:
        data = f.read()
        data = data.replace("\n", "<br>")
        return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
