import pymongo
from pymongo import errors

client = pymongo.MongoClient("mongodb+srv://admin:admin@database.lauyn.mongodb.net/MovieReview?retryWrites=true&w=majority")
db = client.test


b = client.MovieReview.Login.find_one({"email":"yelagandula@gmail.com","password":"12345iuffhjdhdhd"})
try:
    c = client.MovieReview.Login.insert_one({"name":"saiveer","email":"saiveer@gmail.com","password":"1234"})
except errors.DuplicateKeyError:
    print("Email is already taken")
a = client.MovieReview.Login.find()
print(b)
print()
print(db)
print()
for i in a:
    print(i)

    print()
