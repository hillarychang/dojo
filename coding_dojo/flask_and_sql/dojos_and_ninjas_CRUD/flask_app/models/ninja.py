# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo


class Ninja:
    
    db='dojo' #dojo database (in mySQL workbench)

    def __init__( self , db_data ):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.dojos_id = db_data['dojos_id']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ): #data comes from controller_ninjas.py in /create_ninja route
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojos_id, created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s,  %(dojos_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data) #tablename or database name??


    @classmethod
    def get_dojo_id_from_ninja(cls, data):
        query = "SELECT dojos_id FROM ninjas WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return (results[0]['dojos_id'])   #get an integer: returns a list of dictionaries




    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s ;" #%(id)s is the key of the dictionary data and returns id
        results = connectToMySQL(cls.db).query_db(query, data) #query_db returns list of objects
        # print ("here",results)
        return cls(results[0])   

        # class method to remove one user from the database
    @classmethod
    def delete(cls, data ):
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db( query, data )

    # class method to edit one user in the database
    @classmethod
    def update(cls, data ):
        query = "UPDATE ninjas SET first_name = %(fname)s , last_name = %(lname)s  , age = %(age)s , updated_at=NOW() WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db( query, data )