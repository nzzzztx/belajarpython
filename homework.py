from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.f6od9yz.mongodb.net/?retryWrites=true&w=majority')

db = client.dbsparta

db.books.insert_one({
    'title': 'Harry Potter', 
    'author': 'J.K. Rowling', 
    'rating': 90
})

db.books.insert_one({
    'title': 'The Fisherman and Fish', 
    'author': 'Joseph Choi', 
    'rating': 10
})

db.books.insert_one({
    'title': 'Fire in the Water', 
    'author': 'Some Dude', 
    'rating': 5
})

# db.books.update_one(
#     {'title': 'The Fisherman and The Fish'},
#     {'$set': {'author': "Jimmy Kim"}}
# )

# db.books.delete_one({'rating': 90})