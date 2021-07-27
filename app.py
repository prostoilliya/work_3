import os
from flask import Flask, render_template
from cryptography.fernet import Fernet


app = Flask(__name__)


key = Fernet.generate_key()


f = Fernet(key)


token = f.encrypt(b"welcome to geeksforgeeks")
d = f.decrypt(token)


@app.route('/')
def hello_word():
    os.getenv('PASSWORD')
    return "<h1>Hello world!</h1>"


@app.route('/encrypt')
def index():
    return render_template(
        'index.html',
        name=token

    )


@app.route('/decrypt')
def index1():
    return render_template(
        'index.html',
        name3=d

    )


if __name__ == '__main__':
    app.run(debug=True)