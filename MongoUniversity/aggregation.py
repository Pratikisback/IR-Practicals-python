import pprint

from pymongo import MongoClient
import datetime

MONGO_URI = "mongodb+srv://PratikChavan:12345678pratik@cluster0.axzgan9.mongodb.net/?retryWrites=true&w=majority"
Client = MongoClient(MONGO_URI)
db = Client['ItalianCuisine']
collection = db['Pizza']

pizzaa = [
    {"name": "Pepperoni", "size": "small", "price": 19,
     "quantity": 1, "date": datetime.datetime.utcnow()},
    {"name": "Pepperoni", "size": "medium", "price": 20,
     "quantity": 20, "date": datetime.datetime.utcnow()},
    {"name": "Pepperoni", "size": "large", "price": 21,
     "quantity": 30, "date": datetime.datetime.utcnow()},
    {"name": "Cheese", "size": "medium", "price": 13,
     "quantity": 50, "date": datetime.datetime.utcnow()},
    {"name": "Cheese", "size": "large", "price": 14,
     "quantity": 10, "date": datetime.datetime.utcnow()},
    {"name": "Vegan", "size": "small", "price": 17,
     "quantity": 1, "date": datetime.datetime.utcnow()},
    {"name": "Vegan", "size": "medium", "price": 18,
     "quantity": 10, "date": datetime.datetime.utcnow()},
    {"name": "Vegan", "size": "medium", "price": 18,
     "quantity": 10, "date": datetime.datetime.utcnow()},
    {"name": "Cheese", "size": "small", "price": 14,
     "quantity": 1, "date": datetime.datetime.utcnow()}
]

# a = collection.insert_many(pizzaa)
# b = collection.find({})
# pprint.pprint(list(b))


no_of_pizzas = 10
c = collection.aggregate([{"$match": {"size": "small"}},

                          # {"$project": {"": "$name"}},
                          {"$project": {"result": {"$multiply": ["$price", 10]}}}

                          ])
pprint.pprint(list(c))

# pprint.pprint(list(c))
