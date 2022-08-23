from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.sighting import Sighting
from flask_app.models.user import User

app.secret_key = "shhh"



@app.route("/show_sighting_users/<int:id>")  #ID comes from -> check index.html route
def show_sighting_users(id):
    data = {"id":id}
    one_sighting = Sighting.get_one(data)
    current_user = User.get_one({'id':session['user_id']})

    
    # users = User.get_all()



    sighting_with_users = Sighting.get_sightings_with_users(data) #[sighting.PY]gives one specific sighting
        #returns a sighting with a list of users
    # sighting.users
    return render_template("view_sighting.html", sighting_user = sighting_with_users, sighting = one_sighting, users = current_user)


# @app.route("/show/<int:id>") #runs show-one-user page
# def show_one(id):
#     data = {'id':id}
#     sightings = Sighting.get_one(data)

#     user_data = {"id":session['user_id']} # need user's id
#     user = User.get_one(user_data)

#     another_user = User.get_one({'id':sightings.user_id})

#     return render_template("view_sighting.html", one_sighting = sightings, users = user, other_user = another_user)




@app.route("/sighting") #runs add recipe form
def sighting():
    
    sightings = Sighting.get_all()
    data = {"id":session['user_id']} # need user's id
    # user = User.get_user_with_recipes(data) #returns a user with a list of posts

    #ADDED
    user = User.get_user_with_sightings(data) #returns a user with a list of recipes
    return render_template("add_sighting.html", all_sightings = sightings, users = user) 






#route to update
@app.route("/update/<int:id>", methods=["POST"]) #deletes a user, doesn't run a page??
def update_sighting(id):

    if not Sighting.validate_sighting(request.form): #request.form  (check user.py)
        return redirect('/update/<int:id>')

    data = {
        'id':id,
        "location": request.form["location"],
        "what_happened" : request.form["what_happened"],
        "number" : request.form["number"],
        "created_at" : request.form["created_at"]

    }

    Sighting.update(data)
    return redirect('/showUser')
    # return redirect(f'/show/{id}')


@app.route("/edit/<int:id>") #update a user, runs edit page
def edit_sighting(id):

    data = {'id':id}
    sightings = Sighting.get_one(data)
    user = User.get_user_with_sightings({'id':sightings.user_id}) #returns a user with a list of recipes

    return render_template("edit_sighting.html", sighting = sightings, users  = user)






@app.route('/create_sighting', methods=["POST"])
def create_recipe():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    
    if not Sighting.validate_sighting(request.form): #request.form  (check user.py)
        return redirect('/create_sighting') #???

    
    data = {

            "location" : request.form["location"],
            "what_happened" : request.form["what_happened"],
            "number" : request.form["number"],
            "user_id": session['user_id'],
            "created_at": request.form["created_at"] #added this

    }
    # We pass the data dictionary into the save method from the Nina class.
    id = Sighting.save(data)
    return redirect('/showUser') 



@app.route("/delete/<int:id>") #deletes a user, doesn't run a page??
def delete_sighting(id):
    data = {'id':id}
    Sighting.delete(data)
    return redirect('/showUser')