from flask import Flask, request, jsonify

app = Flask(__name__)

# Set your configured API key
CONFIG_API_KEY = "ENTER API KEY GENERATED VIA PYTHON"

@app.route('/')
def home():
    return "<h2> API is running. Use POST /check-key with a JSON payload.</h2>"

@app.route('/check-key', methods=['POST'])
def check_key():
    received_key = request.json.get('api_key')  # Read key from JSON body
    if not received_key:
        return jsonify({"error": "API key is required"}), 400
    if received_key == CONFIG_API_KEY:
        return jsonify({"message": "You entered the right key", "bold": True}), 200
    else:
        return jsonify({"error": "You entered a wrong key", "bold": True}), 403
if __name__ == '__main__':
    app.run(debug=True)
