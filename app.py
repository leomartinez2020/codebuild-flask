from flask import Flask

app = Flask(__name__)


@app.route('/')
def testing():
    return 'Testing flask app'
