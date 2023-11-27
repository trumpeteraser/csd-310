import pymongo
from pymongo import MongoClient
client=MongoClient("mongodb+srv://admin:admin@cluster0.ths4a55.mongodb.net/")
db = client["pytech"]
collection = db["students"]

"""
all_or_one = input('Would you like to see all records? Y or N ')
if all_or_one == ('y' or 'Y'):
    results = collection.find({})
    for x in results:
        print(x)
else:
    id_number = int(input("Enter the ID number you would like to search for: "))
    criteria = {"_id": id_number}
    result = collection.find_one(criteria)
    print("ID:", result["_id"])
    print("First Name:", result.get("First Name"))
    print("Last Name:", result.get("Last Name"))

"""
filter = {"_id": 1007}
new_name = {"$set":{"Last Name":"Edwards"}}
collection.update_one(filter,new_name)
result = collection.find_one(filter)
print("ID:", result["_id"])
print("First Name:", result.get("First Name"))
print("Last Name:", result.get("Last Name"))
