from flask import Flask
import scrape

app = Flask(__name__)

@app.route('/')
def greeting():
    return "<code>GET /url:https://example.com</code>"

@app.route('/<path:url>')
def display_json(url):
    status, message, res = scrape.fetch_title(url)
    return {
        'status': status,
        'message': message,
        'title': res,
        'url': url
    }

if __name__ == '__main__':
    app.run()