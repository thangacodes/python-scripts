from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def default_page():
    return '''<style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: green; }
    </style>
<h1> <style="text-decoration: underline;">Welcome to Flask App Development</h1>'''

@app.route("/about")
def about():
    return render_template("about.html")
    
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
@app.route("/profile")
def profile():
    return render_template("profile.html")
    
# Custom 404 error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
