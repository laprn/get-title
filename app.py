from flask import Flask
import scrape

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, Flask!</p>"

@app.route('/<path:url>')
def display_title(url):
    title = scrape.fetch_title(url)
    return {
        'title': title,
        'url': url
    }

if __name__ == '__main__':
    app.run()