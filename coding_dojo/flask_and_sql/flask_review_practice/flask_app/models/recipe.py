# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app import app
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
        # which is made by invoking the function Bcrypt with our app as an argument
        
import re	# the regex module

class Recipe: # model the class after the user table from our database
    
    db='recipes' #login database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.under = data['under']
        self.description = data['description']
        self.instructions = data['instructions']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']   #should i have this here??? yes. its a hidden input 


    def validate_recipe(recipe):
        is_valid = True # we assume this is true
        if len(recipe['name']) < 1:
            flash("Name must not be blank.")
            is_valid = False
        if len(recipe['under']) < 1:
            flash("Under must not be blank.")
            is_valid = False
        if len(recipe['description']) < 1:
            flash("Description must not be blank.")
            is_valid = False
        if len(recipe['instructions']) < 1:
            flash("Instructions must not be blank.")
            is_valid = False
        return is_valid



    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipe ( name , under, description, instructions, user_id, created_at , updated_at ) VALUES ( %(name)s , %(under)s, %(description)s, %(instructions)s, %(user_id)s , %(created_at)s , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement
        return result
    
        # class method to remove one user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM recipe WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipe;"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []      # Create an empty list to append our instances of users
        for post in results: # Iterate over the db results and create instances of users with cls.
            posts.append( cls(post) )
        return posts #returns list of class objects (list of dictionaries)
            

    @classmethod
    def get_one(cls, id):
        data = {'id': id}
        query = "SELECT * FROM recipe WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return cls(results[0])   


    # if logged in as user, can delete post
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM recipe WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE recipe SET name , under, description, instructions, created_at = %(name)s , %(under)s, %(description)s, %(instructions)s, %(created_at)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )