from flask import render_template, redirect, request, session, flash

from flask_app import app

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.post import Post
from flask_app.models.user import User

app.secret_key = "shhh"



@app.route("/post") #runs starting form
def post():
    
    posts = Post.get_all()
    # all_user = User.get_all()
    data = {"id":session['user_id']} # need user's id
    user = User.get_user_with_posts(data) #returns a user with a list of posts

    return render_template("result.html", all_posts = posts, users = user) 


@app.route('/create_post', methods=["POST"])
def create_post():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    
    if not Post.validate_post(request.form): #request.form  (check user.py)
        return redirect('/post') #???

    
    data = {
        "content": request.form['message'],
        "user_id": session['user_id']
    }
    # We pass the data dictionary into the save method from the Nina class.
    id = Post.save(data)
    return redirect('/post') 


# @app.route("/show_user_posts/<int:id>")  #ID comes from -> check index.html route
# def show_user_posts(id):
#     data = {"id":id}
#     user = User.get_user_with_posts(data) #returns a user with a list of posts
#     return render_template("result.html", users = user)


@app.route("/delete/<int:id>") #deletes a user, doesn't run a page??
def delete_post(id):
    data = {'id':id}
    Post.delete(data)
    return redirect('/post')