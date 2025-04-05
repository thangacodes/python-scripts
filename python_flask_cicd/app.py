from flask import Flask

# Create the Flask app instance (Don't overwrite 'app' with a function)
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"

@app.route("/app")
def app_page():
    return "This is app page!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
