import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://admin:admin@cluster0.ths4a55.mongodb.net/")
db = client["pytech"]
collection = db["students"]

results = collection.find({})

for x in results:
    print(x)

collection.insert_one ({"_id": 1010, "First Name": "Walker", "Last Name": "Texas Ranger"})
filter = {"_id": 1010}
result = collection.find_one(filter)
print("ID:", result["_id"])
print("First Name:", result.get("First Name"))
print("Last Name:", result.get("Last Name"))

collection.delete_one({"_id": 1010})

results = collection.find({})

for x in results:
    print(x)