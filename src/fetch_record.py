import pymongo
from pymongo import MongoClient

client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['record']
record_collection = db['record_collection']

fp = open("record_pos.txt","w")
out_ls = []
for x in record_collection.find({},{"_id":0,"content":1}):
    st=str(1)
    #print(st)
    #print(x['content'])
    out_ls.append(st+" "+str(x['content'])+'\n')
fp.writelines(out_ls)
fp.close()












