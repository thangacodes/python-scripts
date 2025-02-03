from flask import Flask, render_template
import random
import datetime
import logging
app = Flask(__name__)
# Disable Flask development server's logging (Werkzeug)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
@app.route('/')
def index():
    current_date = datetime.datetime.now().strftime ("%d-%m-%Y %H:%M:%S")
    return render_template('index.html', current_date=current_date)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
