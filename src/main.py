import os

from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()

if __name__ == "__about__":
    about()
