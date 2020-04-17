import os
import shutil
import pymongo
from pymongo import MongoClient
import pandas as pd

client = MongoClient()
client = MongoClient('localhost', 27017,maxPoolSize=None)
db = client['preprocessed_book']
record_collection = db['book_collection']
data_list=[]

path = '../data/book_small_preprocessed/'
print(os.listdir(path))
for i in os.listdir(path):        # 藏
    ls_1 = path + i + '/'
    for j in os.listdir(ls_1):    # 部
        data_list=[]
        ls_2 = ls_1 + j + '/'
        for k in os.listdir(ls_2):
            dict={}
            dict['level_1']=i
            dict['level_2']=j
            book_path = ls_2 + k 
            dict['name'] = k
            fp = open(book_path, 'r')
            dict['content'] = fp.read()
            fp.close()
            record_collection.insert_one(dict)
            #data_list.append(dict)
        #record_collection.insert_many(data_list)
  
#print(data_list[0])
# record_collection.insert_many(data_list)










