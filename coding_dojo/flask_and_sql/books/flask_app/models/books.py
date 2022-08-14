# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import authors


class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated']

        # We now create a list so that later we can add in all the author objects that relate to a book.
        self.authors = []

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
                "id" : row_from_db["toppings.id"],
                "topping_name" : row_from_db["topping_name"],
                "created_at" : row_from_db["toppings.created_at"],
                "updated_at" : row_from_db["toppings.updated_at"]
            }
            book.authors.append(authors.Author( author_data ) )
        return book





# class Book:
    
#     db='books' #dojo database (in mySQL workbench)

#     def __init__( self , db_data ):
#         self.id = db_data['id']
#         self.first_name = db_data['first_name']
#         self.last_name = db_data['last_name']
#         self.age = db_data['age']
#         self.created_at = db_data['created_at']
#         self.updated_at = db_data['updated_at']

#     @classmethod
#     def save( cls , data ): #data comes from controller_ninjas.py in /create_ninja route
#         query = "INSERT INTO ninjas ( first_name , last_name, age, dojos_id, created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s,  %(dojos_id)s,NOW(),NOW());"
#         return connectToMySQL(cls.db).query_db(query,data) #tablename or database name??