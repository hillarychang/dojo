from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.books import Book



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







