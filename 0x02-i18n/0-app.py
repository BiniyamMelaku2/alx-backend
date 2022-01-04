#!/usr/bin/python3
""" a script that starts a Flask application """
from flask import Flask, render_template
app = Flask(__name__, static_url_path='')


@app.route('/', methods=['GET'], strict_slashes=False)
def hello() -> str:
    ''' returns a simple page '''
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
