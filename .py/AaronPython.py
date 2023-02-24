## create a Crud Class with a method that inserts a documents into a specified MongoDB collection
# input argument to function will be a set of key/value pairs accetped by MongoDB driver insert API 
# return value true id success full else false 

import pymongo
import sys
import os
import json

class Crud:

    def __init__(self, host, port, db, collection):
        self.host = host
        self.port = port
        self.db = db
        self.collection = collection

    def insert(self, document):
        try:
            client = pymongo.MongoClient(self.host, self.port)
            db = client[self.db]
            collection = db[self.collection]
            collection.insert_one(document)
            return True
        except Exception as e:
            print(e)
            return False 

if __name__ == "__main__":

    # create a Crud object
    crud = Crud("localhost", 27017, "test", "test")

    # create a document to insert
    document = {"name": "John", "age": 30, "city": "New York"}

    # insert the document
    if crud.insert(document):
        print("insert successful")
    else:
        print("insert failed")

    sys.exit(0)

# The above code is a simple example of how to create a class that can be used to insert documents 
# into a MongoDB collection. The class is called Crud and it has a method called insert that takes a 
# document as an argument. The document is a Python dictionary that is accepted by the MongoDB driver 
# insert API. The insert method returns True if the insert is successful and False if the insert fails. 
# The insert method uses the MongoDB driver insert_one method to insert the document into the collection.


