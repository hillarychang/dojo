from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.sighting import Sighting
from flask_app.models.user import User
from flask_app.models.skeptic import Skeptic

app.secret_key = "shhh"





@app.route("/sighting") #runs add recipe form
def sighting():
    
    sightings = Sighting.get_all()
    data = {"id":session['user_id']} # need user's id
    # user = User.get_user_with_recipes(data) #returns a user with a list of posts

    #ADDED
    user = User.get_user_with_sightings(data) #returns a user with a list of recipes
    return render_template("add_sighting.html", all_sightings = sightings, users = user) 


@app.route("/skeptic/<int:id>") #displays all skeptics
def skeptic(id):

    #id is sighting id
    
    data = {'id':id}
    skeptics = Skeptic.get_all()
    # data = {"id":session['user_id']} # need user's id
    # user = User.get_user_with_recipes(data) #returns a user with a list of posts

    #ADDED
    sighting = Sighting.get_sighting_with_skeptics(data) #returns a user with a list of recipes
    return render_template("view_sighting.html", all_skeptics = skeptics, sightings = sighting) 



@app.route('/create_skeptic/<int:id>')
def create_skeptic(id):

    #id is

    data =  {'id':id}
    id = Skeptic.save(data)

    return redirect('/showUser') 


@app.route("/delete/<int:id>") #deletes a user, doesn't run a page??
def delete_skeptic(id):
    
    #id is skeptic id

    data = {'id':id}
    Skeptic.delete(data)
    return redirect('/showUser')