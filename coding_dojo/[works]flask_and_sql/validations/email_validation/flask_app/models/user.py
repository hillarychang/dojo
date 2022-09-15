# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module

class User: # model the class after the user table from our database
    
    db='users' #users database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    

    # # create a regular expression object that we'll use later   
    # @staticmethod
    # def validate_user( user ):
    #     EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
    #     is_valid = True
    #     # test whether a field matches the pattern
    #     if not EMAIL_REGEX.match(user['email']): 
    #         flash("Invalid email address!")
    #         is_valid = False
    #     return is_valid

#validations:
    # Other User methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_user(user):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True # we assume this is true
        if len(user['fname']) < 1:
            flash("First name is required.")
            is_valid = False
        if len(user['lname']) < 1:
            flash("Last name is required.")
            is_valid = False
        if len(user['email']) < 1:
            flash("Email is required.")
            is_valid = False
                # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []      # Create an empty list to append our instances of users
        for user in results: # Iterate over the db results and create instances of users with cls.
            users.append( cls(user) )
        return users #returns list of class objects (list of dictionaries)
            

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM user WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return cls(results[0])   


    # OTHER class methods
    # class method to save our user to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO user ( first_name , last_name  , email, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement

    # class method to remove one user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM user WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE user SET first_name = %(fname)s , last_name = %(lname)s  , email = %(email)s , updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )