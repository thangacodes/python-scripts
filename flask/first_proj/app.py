from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def blog():
    return ''' 
<br> <span style="color: blue; font-weight: bold;"> Welcome to my Blog :) </span> </br> '''

@app.route('/about')
def about():
    return '''
<br> * <span style="color: green; font-weight: bold;"> Hello, I am Thangadurai Murugan and I am based out of Bangalore, India. </span> </br>
<br> * <span style="color: green; font-weight: bold;"> Typically, I work with AWS Cloud Services, Ansible, Jenkins CICD, Docker, Kubernetes, and Python/Shell Scripting automations. </span> </br>
<br> * <span style="color: green; font-weight: bold;"> I enjoy learning new technical skills such as Python/Shell programming to eliminate the manual work of today to automated methods to save time. </span> </br>'''

@app.route('/work')
def work():
    return '''
<br> * <span style="color: green; font-weight: bold;"> I have around 12 years of IT experience and I'm currently focusing on AWS Cloud and DevOps. </span> </br>
<br> * <span style="color: green; font-weight: bold;"> I love learning new technologies and exploring Python and putting my efforts into it. </span> </br> '''

@app.route('/health')
def health():
    return '''
<br> * <span style="color: green; font-weight: bold;"> App is healthy !! </span> </br> 
'''

@app.route('/ping')
def ping():
    return '''
<br> 
<span style="color: green; font-weight: bold;"> Pong is the response back to the user. </span> 
</br> '''

# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 
