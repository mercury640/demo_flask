from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello from Flask_Demo V1</h2>'


if __name__ == "__main__":
    app.run(debug=True)
