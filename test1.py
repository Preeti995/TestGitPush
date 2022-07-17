import pymongo

'''client = pymongo.MongoClient("mongodb+srv://Preeti:Preeti09@mycluster.yg1uk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)'''
client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {"name":"Preeti",
     "email":"preeti9095@gmail.com",
     "surname":"Singh"}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)