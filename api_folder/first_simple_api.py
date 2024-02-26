# Pre-requisites: 
# pip install flask

from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route("/")
def home():
    return "India is my Country!!"
if __name__ == "__main__":
    app.run(debug=True)
