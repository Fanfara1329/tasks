from flask import Flask, render_template, url_for

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


@app.route('/promotion_image')
def pr_im():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='/style.css')}" />
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <title>Колонизация</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/MARS.png">
                        <div class="alert alert-dark" role="alert">
                            <h1 class="alert-heading">Человечество вырастает из детства.</h1>
                        </div>
                        <div class="alert alert-success" role="alert">
                            <h1 class="alert-heading">Человечеству мала одна планета.</h1>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <h1 class="alert-heading">Мы сделаем обитаемыми безжизненные планеты.</h1>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h1 class="alert-heading">И начнём с Марса!</h1>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <h1 class="alert-heading">Присоединяйся!</h1>
                        </div>
                      </body>
                    </html>"""


app.run(port=8080, host='127.0.0.1')
