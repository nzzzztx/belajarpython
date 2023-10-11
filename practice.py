from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.f6od9yz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

# doc1 = {'name': 'bobby', 'age': 21}
# doc2 = {'name': 'kay', 'age': 27}
# doc3 = {'name': 'john', 'age': 30}

# db.users.insert_one(doc1)
# db.users.insert_one(doc2)
# db.users.insert_one(doc3)

# all_users = list(db.users.find({}, {'_id': False}))

# print(all_users)
# print(all_users[o])['name']

# for user in all_users:
#     print(user)

# user = db.users.find_one({ 'name': 'bobby'})
# print(user)

# db.users.update_one({'name': 'bobby'}, {'$set': {'age': 19}})

# db.users.delete_one({'name': 'bobby'})