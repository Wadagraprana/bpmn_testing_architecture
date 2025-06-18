
from bson import ObjectId
from .mongo_client import mongo_db

collection = mongo_db["posts"]

def create_post(data):
    return str(collection.insert_one(data).inserted_id)

def get_post(post_id):
    return collection.find_one({"_id": ObjectId(post_id)})

def update_post(post_id, data):
    return collection.update_one({"_id": ObjectId(post_id)}, {"$set": data})

def delete_post(post_id):
    return collection.delete_one({"_id": ObjectId(post_id)})
