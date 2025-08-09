from flask import Flask, jsonify, request
import subprocess
app = Flask(__name__)

@app.route("/")
def home():
    # Run shell command to get hostname
    try:
      hostname = subprocess.check_output(['hostname']).decode('utf-8').strip()
    except Exception as e:
      hostname = "Unknown (error retrieving hostname)"
      print(f"Error: {e}")
    return f'''
    <h1>
      <span style="color: Green;"> Welcome to the User Page </span>
      <br>
      Running local Flask server on a MacBook Pro and its hostname: {hostname}
    </h1>
    '''

@app.route("/user_create")
def user_create():
  return '''
  <h1>
      <span style="color: blue;"> Welcome to the User Creation page </span>
  </h1> 
  '''

@app.route("/user_delete")
def user_delete():
  return '''
  <h1>
      <span style="color: red;"> Welcome to the User Creation page </span>
  </h1> 
  '''

if __name__ == "__main__":
    app.run(debug=True)
