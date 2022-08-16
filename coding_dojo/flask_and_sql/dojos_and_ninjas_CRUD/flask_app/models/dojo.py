# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo: # model the class after the user table from our database
    db='dojo' #dojo database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
        self.ninjas=[]

    # class method to save our user to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name , created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement
            #cls.db is the database name


    @classmethod
    def get_dojo_with_ninjas( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojos_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db( query , data )
        # results will be a list of topping objects with the ninja attached to each row. 
        dojo = cls( results[0] )
        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            ninja_data = {
                "id" : row_from_db["ninjas.id"],  #ninjas.__ because id overlaps with id in dojo
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "dojos_id": row_from_db['dojos_id'],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )  #looping through rows in table and constructing ninja objects
        return dojo     #returns an object with a list of ninjas inside 



# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []      # Create an empty list to append our instances of users
        for dojo in results: # Iterate over the db results and create instances of users with cls.
            dojos.append( cls(dojo) )
        return dojos #returns list of class objects (list of dictionaries)
            



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return cls(results[0])   


        # class method to remove one user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE dojos SET first_name = %(fname)s , last_name = %(lname)s  , age = %(age)s , updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )

#     @classmethod
#     def get_one(cls, data):
#         query = "SELECT * FROM user WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
#         results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
#         # print ("here",results)
#         return cls(results[0])   


#     # OTHER class methods
#     # class method to remove one user from the database
#     @classmethod
#     def delete(cls, data ):
#         query = "DELETE FROM user WHERE id=%(id)s;"
#         return connectToMySQL(cls.db).query_db( query, data )

#     # class method to edit one user in the database
#     @classmethod
#     def update(cls, data ):
#         query = "UPDATE user SET first_name = %(fname)s , last_name = %(lname)s  , email = %(email)s , updated_at=NOW() WHERE id=%(id)s"
#         return connectToMySQL(cls.db).query_db( query, data )