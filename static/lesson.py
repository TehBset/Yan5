from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="/static/style.css">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1 id="h1_top">Мое предложение:{}</h1>
                    <div class="alert alert-dark" role="alert">
                      На ней что-то есть.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Железо например.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      И вообще классная планета.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      Начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''.format(planet_name)


if __name__ == '__main__':
    app.run(port=8880, host='127.0.0.1')
