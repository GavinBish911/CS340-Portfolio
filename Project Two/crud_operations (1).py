from pymongo import MongoClient
from bson.objectid import ObjectId
import importlib
import crud_operations
importlib.reload(crud_operations)

class AnimalShelter:
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password, host="localhost", port=27017, db="AAC", collection="animals"):
        USER = 'aacuser'
        PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34763
        DB = 'AAC'
        COL = 'animals'
        
        # Initialize the MongoClient to connect to the MongoDB instance
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        """Insert a document into the collection."""
        if data:
            insert_result = self.collection.insert_one(data)
            return insert_result.acknowledged  # Return True if successful
        return False

    def read(self, query={}, limit=0):
        """Query documents from the collection."""
        if query is None:
            query = {}
    
        cursor = self.collection.find(query)
        if limit > 0:
            cursor = cursor.limit(limit)
    
        result = [document for document in cursor]
        return result

    def update(self, query, update_data, multiple=False):
        """Update document(s) in the collection based on a query."""
        if query and update_data:
            if multiple:
                update_result = self.collection.update_many(query, {"$set": update_data})
            else:
                update_result = self.collection.update_one(query, {"$set": update_data})
            return update_result.modified_count  # Return the count of modified documents
        return 0

    def delete(self, query, multiple=False):
        """Delete document(s) from the collection based on a query."""
        if query:
            if multiple:
                delete_result = self.collection.delete_many(query)
            else:
                delete_result = self.collection.delete_one(query)
            return delete_result.deleted_count  # Return the count of deleted documents
        return 0
