import flask

app = flask.Flask(__name__)


@app.route('/hello')
def home():
    return "Hello World"
