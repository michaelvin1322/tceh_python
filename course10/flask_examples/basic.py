from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return 'hello world!'



if __name__ == '__main__':
    app.run()




















# @app.route('/<user>')
# def username(user):
#     return 'hello, user: ' + user