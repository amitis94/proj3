import psycopg2
from pymongo import MongoClient

URI = 'mongodb+srv://amitis:rksk4137@cluster.etbe6rl.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(URI)
DATABASE = 'MovieDB'
mong0_data = client[DATABASE] 

COLLECTION = 'movie_contents' #mvcontents
collection = mong0_data[COLLECTION]

COLLECTION2 = 'movie_company'
collection2 = mong0_data[COLLECTION2]

COLLECTION3 = 'movie_actor'
collection3 = mong0_data[COLLECTION3]

for i in collection3.find()[:1]:
    
    for x in i["companyListResult"]['companyList'][:5]:
        print(x)