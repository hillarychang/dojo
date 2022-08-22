# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import sighting


from flask_app import app
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
        # which is made by invoking the function Bcrypt with our app as an argument
        
import re	# the regex module

class Skeptic: # model the class after the user table from our database
    
    db='new_schema' #login database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']   #should i have this here??? yes. its a hidden input 
        self.sighting_id = data['sighting_id']   #should i have this here??? yes. its a hidden input 
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data ):
        query = "INSERT INTO sighting ( sighting_id, user_id, created_at , updated_at) VALUES ( %(sighting_id)s, %(user_id)s ,NOW(), NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement
        return result


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):

        #*changed this method
        query = "SELECT * FROM skeptic LEFT JOIN sighting ON skeptic.sighting_id = sighting.id;"

        results = connectToMySQL(cls.db).query_db(query)
        
        skeptics = []      # Create an empty list to append our instances of users
        
        print("RESULTS",results)
        for skeptic in results: # Iterate over the db results and create instances of users with cls.
            print ("HERE", skeptic)
            one_skeptic = cls(skeptic)


            sighting_data = {
                "id":skeptic["sighting.id"], 
                "location":skeptic["location"], 
                "what_happened":skeptic["what_happened"],
                "number":skeptic["number"],
                "created_at" :skeptic['sighting.created_at'],
                "updated_at": skeptic['sighting.updated_at']
            }

            one_skeptic.sighting = sighting.Sighting(sighting_data)
            skeptics.append(one_skeptic )
        return skeptics #returns list of class objects (list of dictionaries)



    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM skeptic WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        return cls(results[0])   


    # if logged in as user, can delete post
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM skeptic WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )
