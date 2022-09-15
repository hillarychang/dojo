# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books


class Author:
    db='books' #dojo database (in mySQL workbench)

    def __init__( self , db_data ):
        self.id = db_data['id']
        self.name = db_data['name']

        # we need have a list in case we want to show which books are related to the authors.
        self.on_books = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO authors ( name, created_at , updated_at ) VALUES (%(name)s,NOW(),NOW());" #%(name)s is from the controller
        #INSERT INTO authors ( name, <- from table in mySQL

        return connectToMySQL('books').query_db(query, data)

    # get one author with multiple books
            #  This method will retrieve the specific author along with all the books associated with it.


#same as add_to_author_favorites
    @classmethod
    def add_to_book_favorites( cls , data ): #data comes from controller_ninjas.py in /create_ninja route
        query = "INSERT INTO favorites ( author_id , book_id ) VALUES (%(authors_id)s, %(books_id)s);"
        return connectToMySQL(cls.db).query_db(query,data) #tablename or database name??


    @classmethod
    def get_author_with_books( cls , data ):
        query = "SELECT * FROM authors LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db( query , data )
        # results will be a list of author objects with the book attached to each row. 
        author = cls( results[0] )
        for row_from_db in results:
            # Now we parse the author data to make instances of authors and add them into our list.
            book_data = {
            "id" : row_from_db["books.id"],
            "title" : row_from_db["title"],
            "num_of_pages" : row_from_db["num_of_pages"],
            "created_at" : row_from_db["books.created_at"],
            "updated_at" : row_from_db["books.updated_at"]
            }
            author.on_books.append( books.Book( book_data ) )   #appends book instances to list of books in author  
        return author #returns dictionary: one author with a list of books


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.db).query_db(query)
        authors = []      # Create an empty list to append our instances of users
        for author in results: # Iterate over the db results and create instances of users with cls.
            authors.append( cls(author) )
        return authors #returns list of class objects (list of dictionaries)
            

