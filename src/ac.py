import pymongo
from pymongo import MongoClient
import pandas as pd

filename = '../data/table_3.xlsx'
data = pd.read_excel(filename)
data = data[['year','province','city','content','ref']]

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['record']
record_collection = db['record_collection']

data_list=[]
for i in data.values:
    dict={}
    dict['year']=(int)(float(i[0]))
    dict['province']=i[1]
    dict['city']=i[2]
    dict['content']=i[3]
    dict['ref']=i[4]
    data_list.append(dict)

record_collection.insert_many(data_list)


































