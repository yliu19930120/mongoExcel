from pymongo import MongoClient
from pip._vendor import requests

def get_db():
    #建立连接
    client = MongoClient("localhost", 27017)
    #test,还有其他写法
    db = client.xinpibao
    return db
db = get_db()
FundOp = db.FundOp.find()
url = "http://localhost:9200/xinpibao/fund_op/"
i = 0
for FundOpOrigin in FundOp:
    id = FundOpOrigin['id']
    requests.put(url,FundOpOrigin)
    if(i%100==00 and i!=0):
        print("当前迁移记录数:"+str(i))
    i = i+1
