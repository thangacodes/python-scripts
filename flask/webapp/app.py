from flask import Flask, render_template
import random
import logging
app = Flask(__name__)
# Disable Flask development server's logging (Werkzeug)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)