from flask import render_template, redirect, request, session

from flask_app import app

from flask_app.models.books import Book
from flask_app.models.authors import Author


@app.route("/book") #runs starting form
def book():
    books = Book.get_all()
    return render_template("index-books.html", all_books = books) 

@app.route("/show_book_authors/<int:id>")  #ID comes from -> check index.html route
def show_book_authors(id):
    data = {"id":id}
    authors = Author.get_all()
    books = Book.get_books_with_authors(data) #returns a book with a list of authors
    return render_template("book-favorites.html", book = books, all_authors = authors)


@app.route("/add_favorite_book/<int:id>", methods=["POST"])  
def add_favorite_book(id):
    data = {
    "books_id" : request.form["books_id"],
    "authors_id": id
    }
    Book.add_to_author_favorites(data) #returns a dojo with a list of ninjas
    return redirect(f'/show_author_books/{id}') #redirect goes to route, render_template shows html page


@app.route('/create_book', methods=["POST"])
def create_book():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "title": request.form["title"],
        "num_of_pages" : request.form["num_of_pages"],
    }
    # We pass the data dictionary into the save method from the Nina class.
    id = Book.save(data)
    return redirect('/book') 







