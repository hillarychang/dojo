# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user
from flask_app.models import sighting
from flask_app.models import skeptic

from flask_app import app
from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
        # which is made by invoking the function Bcrypt with our app as an argument
        
import re	# the regex module

class Sighting: # model the class after the user table from our database
    
    db='new_schema' #login database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.what_happened = data['what_happened']
        self.number = data['number']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']   #should i have this here??? yes. its a hidden input 

        self.skeptics = []

    def validate_sighting(sighting):
        is_valid = True # we assume this is true
        if len(sighting['location']) < 1:
            flash("Location must not be blank.")
            is_valid = False
        if len(sighting['what_happened']) < 1:
            flash("Description must not be blank.")
            is_valid = False
        if len(sighting['number']) < 1:
            flash("Number must not be blank.")
            is_valid = False
        return is_valid


    @classmethod
    def get_sighting_with_skeptics( cls , data ):
        query = "SELECT * FROM sighting LEFT JOIN skeptic ON skeptic.sighting_id = sighting.id WHERE sighting.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db( query , data )
        # results will be a list of topping objects with the ninja attached to each row. 
        sighting = cls( results[0] )
        for row_from_db in results:
            # Now we parse the ninja data to make instances of ninjas and add them into our list.
            skeptic_data = {
                "id" : row_from_db["skeptic.id"],  #ninjas.__ because id overlaps with id in dojo
                "sighting_id" : row_from_db['sighting_id'],
                
            }
            sighting.skeptics.append( skeptic.Skeptic( skeptic_data ) )
        return sighting     #returns an object with a list of posts inside 

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO sighting ( location , what_happened, number, user_id, created_at , updated_at ) VALUES ( %(location)s , %(what_happened)s, %(number)s, %(user_id)s , %(created_at)s , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        result = connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement
        return result
    
        # class method to remove one user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM sighting WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):

        #*changed this method
        query = "SELECT * FROM sighting LEFT JOIN user ON sighting.user_id = user.id;"

        results = connectToMySQL(cls.db).query_db(query)
        
        sightings = []      # Create an empty list to append our instances of users
        
        print("RESULTS",results)
        for sighting in results: # Iterate over the db results and create instances of users with cls.
            print ("HERE", sighting)
            one_sighting = cls(sighting)


            user_data = {
                "id":sighting["user.id"], 
                "first_name":sighting["first_name"], 
                "last_name":sighting["last_name"],
                "email":sighting["email"],
                "password":sighting["password"],
                "created_at" :sighting['user.created_at'],
                "updated_at": sighting['user.updated_at']
            }

            one_sighting.user = user.User(user_data)
            sightings.append( one_sighting)
        return sightings #returns list of class objects (list of dictionaries)



    # @classmethod
    # def get_one(cls):

    #     #*changed this method
    #     query = "SELECT * FROM sighting LEFT JOIN user ON sighting.user_id = user.id WHERE id = %(id)s;"
    #     results = connectToMySQL(cls.db).query_db(query)
    
    #     user_data = {
    #         "id":sighting["user.id"], 
    #         "first_name":sighting["first_name"], 
    #         "last_name":sighting["last_name"],
    #         "email":sighting["email"],
    #         "password":sighting["password"],
    #         "created_at" :sighting['user.created_at'],
    #         "updated_at": sighting['user.updated_at']
    #     }

    #     one_sighting.user = user.User(user_data)





    #sighting should have user obj associated
    # @classmethod
    # def get_one(cls, data):
    #     data = {'id': id}

    #     #*changed this method
    #     query = "SELECT * FROM sighting LEFT JOIN user ON sighting.user_id = user.id WHERE id = %(id)s;"

    #     results = connectToMySQL(cls.db).query_db(query)
        
    #     sightings = []      # Create an empty list to append our instances of users
        
    #     print("RESULTS",results)
    #     for sighting in results: # Iterate over the db results and create instances of users with cls.
    #         print ("HERE", sighting)
    #         one_sighting = cls(sighting)


    #         user_data = {
    #             "id":sighting["user.id"], 
    #             "first_name":sighting["first_name"], 
    #             "last_name":sighting["last_name"],
    #             "email":sighting["email"],
    #             "password":sighting["password"],
    #             "created_at" :sighting['user.created_at'],
    #             "updated_at": sighting['user.updated_at']
    #         }

    #         one_sighting.user = user.User(user_data)
    #         sightings.append( one_sighting)
    #     return sightings #returns list of class objects (list of dictionaries)



        # return sightings #returns list of class objects (list of dictionaries)


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM sighting WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        return cls(results[0])   


    # if logged in as user, can delete post
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM sighting WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE sighting SET location = %(location)s, what_happened = %(what_happened)s, number =  %(number)s, created_at =%(created_at)s, updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )