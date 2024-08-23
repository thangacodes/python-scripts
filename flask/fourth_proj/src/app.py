from flask import Flask, render_template, make_response, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/health')
def health():
    data = {'health': 'ok'}
    return jsonify(data), 200

@app.route('/ping')
def ping():
    response = make_response('<span style="color: green; font-weight: bold;">pong</span></br>')
    response.status_code = 200
    return response

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pic')
def leader():
    return render_template('pic.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
