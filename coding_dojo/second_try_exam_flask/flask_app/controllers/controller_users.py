from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.user import User
from flask_app.models.sighting import Sighting

app.secret_key = "shhh"


# controller_authors:add_favorite_author -> show_book_authors
# show_book_authors




@app.route("/create_skeptic/<int:id>") #runs add recipe form
def create_skeptic(id):
    data = {
    "user_id":session['user_id'],
    "sighting_id": id
    } 

    print("SKEPTIC", User.get_one({"id":session['user_id']}).skeptic)


    if (User.get_one({"id":session['user_id']}).skeptic == 0):
        User.add_to_user_skeptics(data)  
        User.get_one({"id":session['user_id']}).set_skeptic()
        print("ok this worked",User.get_one({"id":session['user_id']}).skeptic)

        
    #inset into skeptic
    return redirect(f'/show_sighting_users/{id}') #redirect goes to route, render_template shows html page



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

    print("ID",user_id)
    # store user id into session
    session['user_id'] = user_id
    return redirect("/showUser")



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

    return redirect("/showUser")


@app.route("/showUser") #runs starting form
def showUser():
    
    sightings = Sighting.get_all()
    data = {"id":session['user_id']} # need user's id
    user = User.get_user_with_sightings(data) #returns a user with a list of recipes
    return render_template("result.html", all_sightings = sightings, users = user) 





@app.route("/") #runs starting form
def index():
    return render_template("index.html") 



@app.route("/log_out") 
def log_out():
    session.clear()
    # session["counter"] = 1
    return redirect('/')


