from flask import Flask
'''
it creates an instances of the flask class,
which will be your WSGI application.
'''
##WSGI Application
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/index")
def index():
    return "welcome to the flask course"

@app.route("/motion")
def motion():
    return "This is the data sciennce tutorial"

if __name__ =="__main__":
    app.run(debug=True)