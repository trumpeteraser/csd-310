import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://admin:admin@cluster0.ths4a55.mongodb.net/")
db = client["pytech"]
collection = db["students"]

results = collection.find({})

for x in results:
    print(x)