from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.user import User



@app.route("/") #runs starting form
def index():
    return render_template("index.html") 

@app.route("/show_users") #runs results page
def show_users():
    users = User.get_all()
    return render_template("result.html", all_users = users)

#route to display update page
@app.route("/edit/<int:id>") #update a user, runs edit page
def edit_user(id):
    data = {'id':id}
    users = User.get_one(data)
    return render_template("edit.html", user = users)


@app.route("/show/<int:id>") #runs show-one-user page
def show_one(id):
    data = {'id':id}
    users = User.get_one(data)
    return render_template("show-one.html", user = users)

#route to update
@app.route("/update/<int:id>", methods=["POST"]) #deletes a user, doesn't run a page??
def update_user(id):
    data = {'id':id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }

    User.update(data)
    return redirect(f'/show/{id}')
    # return redirect(f'/edit/{id}')


@app.route("/delete/<int:id>") #deletes a user, doesn't run a page??
def delete_user(id):
    data = {'id':id}
    User.delete(data)
    return redirect('/show_users')


@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the User class.
    id = User.save(data)
    return redirect(f'/show/{id}') 







