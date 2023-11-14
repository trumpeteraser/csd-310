
import pymongo
from pymongo import MongoClient
url="mongodb+srv://admin:admin@cluster0.ths4a55.mongodb.net/"
client=MongoClient(url)
db = client.pytech
print(db.list_collection_names())


