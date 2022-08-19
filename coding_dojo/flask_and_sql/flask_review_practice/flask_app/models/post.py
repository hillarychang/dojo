# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app import app
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
        # which is made by invoking the function Bcrypt with our app as an argument
        
import re	# the regex module

class Post: # model the class after the user table from our database
    
    db='dojo_wall' #login database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']   #should i have this here??? yes. its a hidden input 


    def validate_post(post):
        is_valid = True # we assume this is true
        if len(post['message']) < 1:
            flash("Can't be blank.")
            is_valid = False
        return is_valid


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO posts ( content , user_id, created_at , updated_at ) VALUES ( %(content)s , %(user_id)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement
        print("RESULTS",result)
        return result
    
        # class method to remove one user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM posts WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM posts ORDER BY created_at DESC;"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []      # Create an empty list to append our instances of users
        for post in results: # Iterate over the db results and create instances of users with cls.
            posts.append( cls(post) )
        return posts #returns list of class objects (list of dictionaries)
            

    @classmethod
    def get_one(cls, id):
        data = {'id': id}
        query = "SELECT * FROM posts WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return cls(results[0])   


    # if logged in as user, can delete post
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM posts WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE posts SET content = %(content)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )