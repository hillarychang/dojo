from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User
from flask_app.models.post import Post

app.secret_key = "shhh"

# REGISTRATION
@app.route('/create_user', methods=['POST'])
def create_user():

    if not User.validate_user(request.form): #request.form  (check user.py)
        return redirect('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data = {
        "first_name": request.form['fname'],
        "last_name": request.form['lname'],
        "email": request.form['email'],
        "password" : pw_hash #assign hash to self.password
    }

    user_id = User.save(data)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/show_logged_in")



# LOGIN
@app.route('/login', methods=['POST'])
def login():

    if not User.validate_login(request.form): #request.form  (check user.py)
        return redirect('/')


    data = { "email" : request.form["email"] }

    user_in_db = User.get_by_email(data)

    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect("/")

    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')

    session['user_id'] = user_in_db.id #create session with user_in_db.id 

    return redirect("/show_logged_in")



@app.route("/") #runs starting form
def index():
    return render_template("index.html") 

#route to display page
@app.route("/show_logged_in") 
def show_logged_in():
    # data = {'id':session['user_id']}
    print("HERE",session['user_id'])
    users = User.get_one(session['user_id'])
    return render_template("result.html", user = users)



@app.route("/log_out") 
def log_out():
    session.clear()
    session["counter"] = 1
    return redirect('/')


