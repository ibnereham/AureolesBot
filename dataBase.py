
from pymongo.mongo_client import MongoClient
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

uri = os.getenv("MONGODB_AU_URL")

try:
    client = MongoClient(uri)
except pymongo.errors.ConfigurationError:
  print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")


db = client["user"]
collection = db['info']

def CheckIfUserIsAlreadyHere(user_id):
    post = {"_id":user_id}
    available = collection.find_one(post)
    if available:
        return True
    else:
        return False
def RegisterUser(user_id):
    post = {"_id":user_id,"warns":0}
    collection.insert_one(post)

def finduser(user_id):
    post = {"_id":user_id}
    user = collection.find_one(post)
    return user
def findUserWarns(uid):
    post = {"_id":uid}
    user = collection.find_one(post)['warns']
    if user < 0:
        y = 0-user
        for i in range(y):
            addOneWarn(uid)
    return user

def deleteuser(uid):
    post = {"_id":uid}
    collection.delete_one(post)
def addOneWarn(uid):
    filter = {"_id": uid}
    update = {"$inc": {"warns": 1}}
    try:
        result = collection.update_one(filter, update)
    except pymongo.errors.PyMongoError as e:
        raise e  

    if result.matched_count == 0:
        print(f"User with ID {uid} not found. No warning added.")
        RegisterUser(uid)
        addOneWarn(uid)
    else:
        print(f"Warning added for user ID: {uid}")
def resetWarns(uid):
    x = CheckIfUserIsAlreadyHere(uid)
    if x:
        deleteuser(uid)
        RegisterUser(uid)
        return True
    else:
        return False

def removeOneWarn(user_id):
   
    filter = {"_id": user_id}
    update = {"$inc": {"warns": -1}} 

    try:
        result = collection.update_one(filter, update)
    except pymongo.errors.PyMongoError as e:
        raise e  

    if result.matched_count == 0:
        RegisterUser(user_id)
        if findUserWarns(user_id)<=0:
            print(f"User ID: {user_id} already has 0 warnings. No change made.")
            return False

        removeOneWarn(user_id)
        return True
    elif result.modified_count == 0:
        print(f"User ID: {user_id} already has 0 warnings. No change made.")
        return False
    else:
        print(f"Warning removed for user ID: {user_id}")
        return True




