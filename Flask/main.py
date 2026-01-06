from flask import Flask,render_template

'''
it creates an instances of the flask class,
which will be your WSGI application.
'''
##wsgi application 
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ =="__main__":
    app.run(debug=True)