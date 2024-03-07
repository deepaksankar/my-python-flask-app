import os

from flask import Flask, send_file, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('index.html')

@app.route("/about")
def about():
    return render_template('about.html', num=5)

@app.route("/your-url", methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        urls[request.form['code']] = {'url': request.form['url']}
        with open('urls.json', 'w') as file:
            json.dump(urls, file)
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('index'))

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()

if __name__ == "__about__":
    about()
