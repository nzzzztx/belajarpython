from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.f6od9yz.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta 


# target_movie = db.movies.find_one({'movie: "The Matrix'})
# # print(target_movie['rating'])
# target_rating = target_movie['rating']

# movies = list(db.movies.find({'rating' : target_rating}))

# for movie in movies:
#     print(movie['movie'])

# db.movies.update_one(
#     {'movie': 'The Matrix'},
#     {'$set': {'rating': '0'}}
# )

# movie = db.movies.find_one({'movie': 'The Matrix'})

# print(movie['rating'])