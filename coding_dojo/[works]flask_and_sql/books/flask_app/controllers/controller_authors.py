from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.authors import Author
from flask_app.models.books import Book



@app.route("/") #runs starting form
def index():
    authors = Author.get_all()
    return render_template("index.html", all_authors = authors) 


@app.route("/show_author_books/<int:id>")  #ID comes from -> check index.html route
def show_author_books(id):
    data = {"id":id}
    books = Book.get_all()
    authors = Author.get_author_with_books(data) #returns a author with a list of books
    return render_template("author-favorites.html", author = authors, all_books = books)

@app.route("/add_favorite_author/<int:id>", methods=["POST"])  
def add_favorite_author(id):
    data = {
    "authors_id" : request.form["authors_id"], #gets from <select name="authors_id">, returns value = {{author.id}} 
    "books_id": id
    }
    Author.add_to_book_favorites(data) #returns a dojo with a list of ninjas
    return redirect(f'/show_book_authors/{id}') #redirect goes to route, render_template shows html page



@app.route('/create_author', methods=["POST"])
def create_author():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"]
    }
    # We pass the data dictionary into the save method from the Dojo class.
    id = Author.save(data)
    return redirect('/') 







