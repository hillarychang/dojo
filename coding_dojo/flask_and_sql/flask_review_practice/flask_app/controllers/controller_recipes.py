from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.recipe import Recipe
from flask_app.models.user import User

app.secret_key = "shhh"



@app.route("/recipe") #runs add recipe form
def recipe():
    
    recipes = Recipe.get_all()
    data = {"id":session['user_id']} # need user's id
    # user = User.get_user_with_recipes(data) #returns a user with a list of posts

    return render_template("add_recipe.html", all_recipes = recipes) 


@app.route("/show/<int:id>") #runs show-one-user page
def show_one(id):
    data = {'id':id}
    recipes = Recipe.get_one(data)
    return render_template("view_recipe.html", one_recipe = recipes)



#route to update
@app.route("/update/<int:id>", methods=["POST"]) #deletes a user, doesn't run a page??
def update_recipe(id):

    if not Recipe.validate_recipe(request.form): #request.form  (check user.py)
        return redirect('/update/<int:id>')

    data = {
        'id':id,
        "name": request.form["name"],
        "description" : request.form["description"],
        "instructions" : request.form["instructions"],
        "under" : request.form["under"]
    }

    Recipe.update(data)
    return redirect('/showUser')
    # return redirect(f'/show/{id}')


@app.route("/edit/<int:id>") #update a user, runs edit page
def edit_recipe(id):
    data = {'id':id}
    recipes = Recipe.get_one(data)
    return render_template("edit_recipe.html", recipe = recipes)






@app.route('/create_recipe', methods=["POST"])
def create_recipe():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    
    if not Recipe.validate_recipe(request.form): #request.form  (check user.py)
        return redirect('/create_recipe') #???

    
    data = {

            "name" : request.form["name"],
            "under" : request.form["under"],
            "description" : request.form["description"],
            "instructions" : request.form["instructions"],
            "user_id": session['user_id'],
            "created_at": request.form["created_at"] #added this

    }
    # We pass the data dictionary into the save method from the Nina class.
    id = Recipe.save(data)
    return redirect('/showUser') 


# @app.route("/show_user_posts/<int:id>")  #ID comes from -> check index.html route
# def show_user_posts(id):
#     data = {"id":id}
#     user = User.get_user_with_posts(data) #returns a user with a list of posts
#     return render_template("result.html", users = user)


@app.route("/delete/<int:id>") #deletes a user, doesn't run a page??
def delete_recipe(id):
    data = {'id':id}
    Recipe.delete(data)
    return redirect('/showUser')