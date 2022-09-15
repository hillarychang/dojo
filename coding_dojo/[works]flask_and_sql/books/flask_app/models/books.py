# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import authors


class Book:

    db='books' #dojo database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # We now create a list so that later we can add in all the author objects that relate to a book.
        self.authors = []


#same as add_to_book_favorites
    @classmethod
    def add_to_author_favorites( cls , data ): #data comes from controller_ninjas.py in /create_ninja route
        query = "INSERT INTO favorites ( author_id , book_id ) VALUES (%(authors_id)s, %(books_id)s);"
        return connectToMySQL(cls.db).query_db(query,data) #tablename or database name??


    @classmethod
    def save( cls , data ): #data comes from controller_ninjas.py in /create_ninja route
        query = "INSERT INTO books ( title , num_of_pages, created_at , updated_at ) VALUES (%(title)s, %(num_of_pages)s, NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data) #tablename or database name??



    # This method will retrieve the book with all the authors that are associated with the book.
    @classmethod
    def get_books_with_authors( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN authors ON favorites.author_id = authors.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db( query , data )
        # results will be a list of author objects with the book attached to each row. 
        book = cls( results[0] )
        for row_from_db in results:
            
            # Now we parse the author data to make instances of authors and add them into our list.
            author_data = {
                "id" : row_from_db["authors.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.authors.append(authors.Author( author_data ) )
        return book #^get a list of authors that favorited the book

# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.db).query_db(query)
        books = []      # Create an empty list to append our instances of users
        for book in results: # Iterate over the db results and create instances of users with cls.
            books.append( cls(book) )
        return books #returns list of class objects (list of dictionaries)
            

