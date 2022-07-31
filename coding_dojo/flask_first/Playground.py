from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def index():
    return render_template("index.html")	

@app.route('/play/<int:x>')
def boxes(x):
    return render_template("boxes.html", x=x)

@app.route('/play/<int:x>/<string:color>')
def change_color(x, color):
    return render_template("boxes.html", x=x, color=color)	

if __name__=="__main__":
    app.run(debug=True)
    
    
    
# from flask import Flask  # Import Flask to allow us to create our app
# app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# @app.route('/hello/<play>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(play):
#     print(play)
#     return "Hello, " + play

# @app.route('/users/<string:play>/<int:x>') # for a route '/users/____/____', two parameters in the url get passed as username and id
# def show_user_profile(play, x):
#     print(play)
#     print(x)
#     return "Hello, "+(play*x)

# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.


