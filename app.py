from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def root():
    return "Working"

if __name__ == "__main__":
    app.run(debug = False,host="0.0.0.0", port=5000)
