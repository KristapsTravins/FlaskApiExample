from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)


# created  instance

@app.route('/')
@app.route('/hello/<name>')
def hello():
    return render_template('index.html')


@app.errorhandler(404)
def error(error):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

