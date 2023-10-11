from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.f6od9yz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

doc = {
    'name': 'bob',
    'age': 27
}

db.users.insert_one(doc)

