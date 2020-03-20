from django.db import models

# Create your models here.
import pymongo


HOST = '127.0.0.1'
PORT = 27017
DATABASE = 'materialsData'

client = pymongo.MongoClient(host=HOST, port=PORT)
db = client.get_database(name=DATABASE)


def SavaData(dataName, dictList):
    n = 0
    if dataName in db.list_collection_names():
        n += 1
        dataName = dataName[:dataName.rfind('.')] + str(n)
        while dataName in db.list_collection_names():
            n += 1
            dataName = dataName + str(n)

    coll = db.create_collection(name=dataName)
    return coll.insert_many(dictList)
