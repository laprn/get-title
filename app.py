from flask import Flask
from fetchhtmlinfo import fetch_header

app = Flask(__name__)

@app.route('/')
def greeting():
    return "<code>GET /url:https://example.com</code>"

@app.route('/<path:url>')
def display_json(url):
    result = fetch_header.fetch_title(url)
    return result

if __name__ == '__main__':
    app.run()