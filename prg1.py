import pymongo
client = pymongo.MongoClient("mongodb+srv://nikhilkathane97:Niks25252@cluster0.3pjvq.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
    "name": "nikhil",
    "email":"nikhilkathane97@gmail.com",
    "surname":"kathane"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)