import pprint

# import datetime
# from pymongo import MongoClient
#
# MONGO_URI = "mongodb+srv://PratikChavan:12345678pratik@cluster0.axzgan9.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient(MONGO_URI)
# db = client['BankDB']
# collection = db['AccountHolders']
#
# new_account = {"AccountHolder": "Pratik Chavan",
#                "Account_id": "MDBB29001337",
#                "Account_type": "Current",
#                "Account_Balance": 35000,
#                "Last-Updated": datetime.datetime.utcnow()}

# result = collection.insert_one(new_account)
# if result:
#     print("success")
# document_ids = result.inserted_id
# print(document_ids)
from bson import ObjectId

# filter


# projection


# new_accounts_list = [
#     {"AccountHolder": "Vinay Gavhane",
#      "Account_id": "DSFBDVCB9821",
#      "Account_type": "Savings",
#      "Account_Balance": 54200,
#      "Last-Updated": datetime.datetime.utcnow()},
#     {"AccountHolder": "Vishal Rao",
#      "Account_id": "SDFILUSDUI987",
#      "Account_type": "Checking",
#      "Account_Balance": 42000,
#      "Last-Updated": datetime.datetime.utcnow()}
# ]

# result = collection.insert_many(new_accounts_list)
# if result:
#     print('Accounts added successfully')
#     a = result.inserted_ids
#     print(a)
# print("No of documents inserted are  "+ str(len(a)))
#
# doc_to_find = {"_id":ObjectId("647ede9b25d4424cbef37d90")}
# a = collection.find_one(doc_to_find)
# if a:
#     pprint.pprint(a)
#

#
# c = collection.find({}, {"AccountHolder": 1, "Account_Balance": 1, "_id": 0})
# print(c)
# for doc in c:
#     print(doc)
#
# doc_to_find = {"Account_Balance": {"$gt": 40000}}
# d = collection.find(doc_to_find)
# print(d)
#
# # num_of_docs = 0
# for doc in d:
#     # num_of_docs += 1
#     pprint.pprint(doc)

# doc_to_update= {"_id": ObjectId("647f096ece4cd59f249e1788")}
# updateaa = {"$inc": {"Account_Balance": 10900}}
#
# naaa= collection.find_one(doc_to_update)
# pprint.pprint(naaa)
#
# f = collection.update_one(doc_to_update, updateaa)
# pprint.pprint(f.modified_count)
#
# saaa = collection.find_one(doc_to_update)
# pprint.pprint(saaa)



import pandas as pd

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
   'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
   'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
   'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
   'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

print(df)


a = df.groupby('Rank').agg({'Year':'first'}).reset_index()
print(a)
