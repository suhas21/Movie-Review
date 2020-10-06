import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("mongodb+srv://admin:admin@database.lauyn.mongodb.net/MovieReview?retryWrites=true&w=majority")

if client.MovieReview.Login.find_one({"email":"yelagandula@gmail.com","password":"1234"}):
    p = client.MovieReview.Login.find_one({"email":"yelagandula@gmail.com","password":"1234"})
    print(p['_id'])
    x = str(p.get('_id'))
    client.MovieReview.Login.update_one(
    {"_id":ObjectId(x)},
    {"$push":{"history":"ABC"}}
    )
    p = client.MovieReview.Login.find_one({"email":"yelagandula@gmail.com","password":"1234"})
    for i in range(len(p['history'])):
        print(p['history'][i])
    print(p['history'])
