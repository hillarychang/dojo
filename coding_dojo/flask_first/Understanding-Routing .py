
from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # localhost:5000/ - have it say "Hello World!"
def hello_world():
    return 'Hello World!'  

@app.route('/dojo')          # localhost:5000/dojo - have it say "Dojo!"
def dojo():
    return 'Dojo'

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<string:username>/<int:num>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, num):
    print(username)
    print(num)
    return "Hello, "+(username*num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

