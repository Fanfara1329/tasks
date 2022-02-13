from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def first():
    return '<h1>Миссия Колонизация Марса</h1>'
@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


app.run(port=8080, host='127.0.0.1')