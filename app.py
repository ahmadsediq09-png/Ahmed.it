from os import name

from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    if request.method == 'POST':
        url = request.form['url']
        s = pyshorteners.Shortener()
        try:
            short_url = s.tinyurl.short(url)
            return render_template('index.html', short_url=short_url, original_url=url)
        except:
            return render_template('index.html', error="ببورە، شاشیەک هەبوو د لینکێ دا!")

if name == '__main__':
    app.run(debug=True)