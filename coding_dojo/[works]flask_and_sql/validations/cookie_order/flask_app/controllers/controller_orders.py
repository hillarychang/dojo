from flask import render_template, redirect, request, session, url_for, flash

from flask_app import app

from flask_app.models.orders import Order



@app.route("/") #runs show all page
def index():
    return redirect('/cookies')
    
@app.route("/cookies") #runs show all page
def cookies():
    orders = Order.get_all()
    return render_template("index.html", all_orders = orders) 



@app.route("/cookies/new") #runs show all page
def show_form():
    return render_template("new.html") 


# @app.route("/show_orders") #runs show all page
# def show_orders():
#     orders = Order.get_all()
#     return render_template("index.html", all_orders = orders) 


#route to display update page
@app.route("/edit/<int:id>") #update a user, runs edit page
def edit_order(id):
    data = {'id':id}
    orders = Order.get_one(data)
    return render_template("edit.html", order = orders)


# @app.route("/show/<int:id>") #runs show-one-user page
# def show_one(id):
#     data = {'id':id}
#     orders = Order.get_one(data)
#     return render_template("show-one.html", order = orders)

#route to update
@app.route("/update/<int:id>", methods=["POST"]) #deletes a user, doesn't run a page??
def update_order(id):
    if not Order.validate_order(request.form): #request.form  (check user.py)
        # return redirect(url_for('update_order'))
        return redirect(f'/edit/{id}')

    data = {'id':id,
        "name": request.form["name"],
        "type" : request.form["type"],
        "number_of_boxes" : request.form["number_of_boxes"]
    }

    Order.update(data)
    return redirect('/')



@app.route('/create_order', methods=["POST"])
def create_order():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    if not Order.validate_order(request.form): #request.form  (check user.py)
        return redirect('/cookies/new')

    data = {
        "name": request.form["name"],
        "type" : request.form["type"],
        "number_of_boxes" : request.form["number_of_boxes"]
    }
    # We pass the data dictionary into the save method from the User class.
    id = Order.save(data)
    return redirect('/') 







