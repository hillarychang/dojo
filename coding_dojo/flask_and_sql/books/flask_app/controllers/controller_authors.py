from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.authors import Author



@app.route("/") #runs starting form
def index():
    dojos = Dojo.get_all()
    return render_template("index.html", all_dojos = dojos) 


@app.route("/show_dojo_ninjas/<int:id>")  #ID comes from -> check index.html route
def show_dojo_ninjas(id):
    data = {"id":id}
    dojos = Dojo.get_dojo_with_ninjas(data) #returns a dojo with a list of ninjas
    return render_template("show-dojo.html", dojo = dojos)



@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    id = Dojo.save(data)
    return redirect('/') 







