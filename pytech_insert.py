import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://admin:admin@cluster0.ths4a55.mongodb.net/")
db = client["pytech"]
collection = db["students"]

post1 = {"_id": 1007, "First Name": "Bilbo", "Last Name": "Baggins"}
post2 = {"_id": 1008, "First Name": "Donald", "Last Name": "Trump"}
post3 = {"_id": 1009, "First Name": "Rick", "Last Name": "Astley"}

collection.insert_many([post1, post2, post3])
