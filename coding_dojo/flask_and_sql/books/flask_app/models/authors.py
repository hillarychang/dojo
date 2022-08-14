# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books


class Author:
    def __init__( self , db_data ):
        self.id = db_data['id']
        self.author_name = db_data['author_name']

        # we need have a list in case we want to show which books are related to the authors.
        self.on_books = []
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ):
        query = "INSERT INTO authors ( author_name, created_at , updated_at ) VALUES (%(author_name)s,NOW(),NOW());"
        return connectToMySQL('books').query_db(query, data)

    # This method will retrieve the specific author along with all the books associated with it.
    @classmethod
    def get_author_with_books( cls , data ):
        query = "SELECT * FROM author LEFT JOIN favorites ON favorites.author_id = authors.id LEFT JOIN books ON favorites.book_id = books.id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db( query , data )
        # results will be a list of author objects with the book attached to each row. 
        author = cls( results[0] )
        for row_from_db in results:
            # Now we parse the author data to make instances of authors and add them into our list.
            book_data = {
            "id" : row_from_db["burgers.id"],
            "name" : row_from_db["name"],
            "bun" : row_from_db["bun"],
            "calories" : row_from_db["calories"],
            "created_at" : row_from_db["toppings.created_at"],
            "updated_at" : row_from_db["toppings.updated_at"]
            }
        author.on_books.append( books.Book( book_data ) )
        return author






# class Author: # model the class after the user table from our database
#     db='books' #dojo database (in mySQL workbench)

#     def __init__( self , data ):
#         self.id = data['id']
#         self.name = data['name']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']
    
#         self.ninjas=[]

#     # class method to save our user to the database
#     @classmethod
#     def save(cls, data ):
#         query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
#         # data is a dictionary that will be passed into the save method from server.py
#         return connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement
#             #cls.db is the database name


#     @classmethod
#     def get_dojo_with_ninjas( cls , data ):
#         query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
#         results = connectToMySQL(cls.db).query_db( query , data )
#         # results will be a list of topping objects with the ninja attached to each row. 
#         dojo = cls( results[0] )
#         for row_from_db in results:
#             # Now we parse the ninja data to make instances of ninjas and add them into our list.
#             ninja_data = {
#                 "id" : row_from_db["ninjas.id"],  #ninjas.__ because id overlaps with id in dojo
#                 "first_name" : row_from_db["first_name"],
#                 "last_name" : row_from_db["last_name"],
#                 "age" : row_from_db["age"],
#                 "created_at" : row_from_db["ninjas.created_at"],
#                 "updated_at" : row_from_db["ninjas.updated_at"]
#             }
#             dojo.ninjas.append( ninja.Ninja( ninja_data ) )
#         return dojo     #returns an object with a list of ninjas inside 



# # Now we use class methods to query our database
#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM dojos;"
#         results = connectToMySQL(cls.db).query_db(query)
#         dojos = []      # Create an empty list to append our instances of users
#         for dojo in results: # Iterate over the db results and create instances of users with cls.
#             dojos.append( cls(dojo) )
#         return dojos #returns list of class objects (list of dictionaries)
            
