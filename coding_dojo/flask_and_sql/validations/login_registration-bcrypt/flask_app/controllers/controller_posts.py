from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.post import Post
from flask_app.models.user import User

app.secret_key = "shhh"

# REGISTRATION
@app.route('/create_post', methods=['POST'])
def create_post():

    if not Post.validate_post(request.form): #request.form  (check user.py)
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['email'],
        "password" : pw_hash #assign hash to self.password
    }

    post_id = Post.save(data)
    # store user id into session
    session['post_id'] = post_id
    return redirect("/show_logged_in")



@app.route("/") #runs starting form
def index():
    return render_template("index.html") 

#route to display page
@app.route("/show_logged_in") 
def show_logged_in():
    # data = {'id':session['user_id']}
    users = User.get_one(session['user_id'])
    return render_template("result.html", user = users)











