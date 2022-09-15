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
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']

    @classmethod
    def save( cls , data ): #data comes from controller_ninjas.py in /create_ninja route
        query = "INSERT INTO ninjas ( first_name , last_name, age, dojos_id, created_at , updated_at ) VALUES (%(fname)s, %(lname)s, %(age)s,  %(dojos_id)s,NOW(),NOW());"
        return connectToMySQL(cls.db).query_db(query,data) #tablename or database name??