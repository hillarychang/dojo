from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



@app.route("/ninja") #runs starting form
def ninja():
    dojos = Dojo.get_all()
    return render_template("new-ninja.html", all_dojos = dojos) 


@app.route('/create_ninja', methods=["POST"])
def create_ninja():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"],
        "dojos_id" : request.form["dojos_id"]
    }
    # We pass the data dictionary into the save method from the Nina class.
    id = Ninja.save(data)
    return redirect('/') 



# CRUD
#route to update
#route to display update page
@app.route("/edit/<int:id>") #update a user, runs edit page
def edit_ninja(id):
    data = {'id':id}
    ninjas = Ninja.get_one(data)
    return render_template("edit.html", ninja = ninjas)
    
@app.route("/update/<int:id>", methods=["POST"]) #deletes a user, doesn't run a page??
def update_ninja(id):
    data = {'id':id,
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "age" : request.form["age"]
    }

    Ninja.update(data)
    dojo_id = Ninja.get_one({'id':id}).dojos_id    

    # dojo_id = Ninja.get_dojo_id_from_ninja({'id':id})
    return redirect(f'/show_dojo_ninjas/{dojo_id}')


@app.route("/delete/<int:id>") #deletes a user, doesn't run a page??
def delete_ninja(id):
    data = {'id':id}
    dojo_id = Ninja.get_dojo_id_from_ninja({'id':id})

    Ninja.delete(data)


    return redirect(f'/show_dojo_ninjas/{dojo_id}')






