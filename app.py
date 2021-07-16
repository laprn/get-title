from flask import Flask, render_template, request
from flask.wrappers import Request
from fetchhtmlinfo import fetch_header

app = Flask(__name__)

@app.route('/')
def greeting():
    return render_template('index.html')

@app.route('/<path:url>')
def display_json_curl(url):
    result = fetch_header.fetch_title(url)
    return result

@app.route('/search')
def display_json_form():
    url = request.args.get('url')
    result = fetch_header.fetch_title(url)
    return result

if __name__ == '__main__':
    app.run()