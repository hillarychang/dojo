# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module

class Order: # model the class after the user table from our database
    
    db='cookies' #users database (in mySQL workbench)

    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.type = data['type']
        self.number_of_boxes = data['number_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
#validations:
    # Other User methods up yonder.
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_order(order):
        # EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True # we assume this is true
        if len(order['name']) < 1:
            flash("Name is required.")
            is_valid = False
        if len(order['type']) < 1:
            flash("Cookie type is required.")
            is_valid = False
        if (len(order['number_of_boxes']) == 0):
            flash("Number of boxes is required.")
            is_valid = False
        else:
            if (int(order['number_of_boxes']) < 0):
                flash("Please enter a valid number.")
                is_valid = False
        # if len(str(order['number_of_boxes'])) < 1:
        #     flash("Number of boxes is required.")
        #     is_valid = False


            # test whether a field matches the pattern
        # if not EMAIL_REGEX.match(order['email']): 
        #     flash("Invalid email address!")
        #     is_valid = False
        return is_valid


# Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM orders;"
        results = connectToMySQL(cls.db).query_db(query)
        orders = []      # Create an empty list to append our instances of users
        for order in results: # Iterate over the db results and create instances of users with cls.
            orders.append( cls(order) )
        return orders #returns list of class objects (list of dictionaries)
            

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM orders WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return cls(results[0])   


    # OTHER class methods
    # class method to save our user to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO orders ( name , type  , number_of_boxes, created_at, updated_at ) VALUES ( %(name)s , %(type)s , %(number_of_boxes)s , NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(cls.db).query_db( query, data )  # returns an ID because of insert statement


    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE orders SET name = %(name)s , type = %(type)s  , number_of_boxes = %(number_of_boxes)s , updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )