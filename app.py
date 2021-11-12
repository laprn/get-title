from flask import Flask, render_template, request, flash, redirect, url_for
from flask.wrappers import Request
from fetchhtmlinfo import fetch_header

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:url>')
def display_json_curl(url):
    result = fetch_header.fetch_title(url)
    return result

@app.route('/search')
def display_json_form():
    url = request.args.get('url')
    result = fetch_header.fetch_title(url)
    flash(result)
    return redirect(url_for('index'))
    # return result

if __name__ == '__main__':
    app.run()
