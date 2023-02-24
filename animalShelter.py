from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections.
        if username and password:
            print ("Your Username and Password is:", username, password)
            # where xxxx is your unique port number
            self.client = MongoClient('mongodb://%s:%s@localhost:39040/AAC' % (username, password))
            self.database = self.client['AAC']
            print ("Connection Was Successful") 
            
            # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data:
            self.database.animals.insert(data)  # data should be dictionary
            return "True"
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
    def read(self, key_value_lookup):
        return self.database.animals.find(key_value_lookup)   
            



