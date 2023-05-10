#Simplest app.py code for demo
from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "<h1>Hello from Flask & Docker</h2>"
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000)
