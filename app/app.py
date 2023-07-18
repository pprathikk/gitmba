# app.py
from flask import Flask, render_template, jsonify

app = Flask(__name__)

data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"},
    {"id": 3, "name": "Item 3"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/data')
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
