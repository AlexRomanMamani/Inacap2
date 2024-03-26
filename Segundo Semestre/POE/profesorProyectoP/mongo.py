import pymongo

mongo_host="localhost"
mongo_puerto="27017"
mongo_tf=1000
mongo_uri="mongodb://"+mongo_host+":"+mongo_puerto+"/"
try:
      
    cliente=pymongo.MongoClient(mongo_uri,ServerSelectionTimeoutMs=mongo_tf)
    BaseDD=cliente["curso"]
    Collec=BaseDD["usuarios"]
    for docu in Collec.find():
        print(docu)
        
    cliente.server_info()
    print("Ok")
    cliente.close()
except  pymongo.errors.ServerSelectionTimeoutError()   as errortiempo:
    print("Error")