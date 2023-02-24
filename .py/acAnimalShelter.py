from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Constructor to initialize MongoClient
        # It takes `username` and `password` to connect to the MongoDB database and collections
        if username and password:
            print("Your Username and Password is:", username, password)
            # Connection to MongoDB on local machine
            # 39040 is the port number for the MongoDB server
            # 'AAC' is the name of the database that we are using
            self.client = MongoClient('mongodb://%s:%s@localhost:39040/AAC' % (username, password))
            self.database = self.client['AAC']
            print("Connection Was Successful") 
            
    # Create method to insert data into the 'animals' collection
    def create(self, data):
        # It takes 'data' parameter as a dictionary
        if data:
            # Inserts 'data' into the 'animals' collection
            self.database.animals.insert(data)  
            return "True"
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
    # Read method to read data from the 'animals' collection
    def read(self, key_value_lookup):
        # The method returns all the documents in the 'animals' collection
        # It excludes the '_id' field from the result set
        return self.database.animals.find(key_value_lookup, {"_id": False})
    
    # Update method to update data in the 'animals' collection
    def update(self, key_value_lookup, updated_data):
        # It takes 'key_value_lookup' parameter to find the data to be updated
        # It takes 'updated_data' parameter to replace the old data
        if key_value_lookup and updated_data:
            # Updates the 'animals' collection with the new data
            self.database.animals.update_one(key_value_lookup, {"$set": updated_data})
            return "True"
        else:
            raise Exception("Nothing to update, because key_value_lookup or updated_data parameter is empty")
        
    # Delete method to delete data from the 'animals' collection
    def delete(self, key_value_lookup):
        # It takes 'key_value_lookup' parameter to find the data to be deleted
        if key_value_lookup:
            # Deletes the data from the 'animals' collection
            self.database.animals.delete_one(key_value_lookup)
            return "True"
        else:
            raise Exception("Nothing to delete, because key_value_lookup parameter is empty")
