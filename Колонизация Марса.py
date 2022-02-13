from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def first():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h1>И на Марсе будут яблони цвести!</h1>'


@app.route('/promotion')
def pro():
    phrase = ['<h1>Человечество вырастает из детства.</h1>', '<h1>Человечеству мала одна планета.<h1>',
              '<h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>', '<h1>И начнем с Марса!</h1>',
              '<h1>Присоединяйся!</h1>']
    return '</br>'.join(phrase)


@app.route('/image_mars')
def im():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <figure>
                        <img src="static/MARS.png">
                    </figure>
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""

app.run(port=8080, host='127.0.0.1')
