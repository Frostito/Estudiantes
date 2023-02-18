import pymongo
import os

class DbMongo:
    
    @staticmethod
    def getDB():
        user = os.environ['Frostito']
        password = os.environ['Frostydb']
        cluster = os.environ['@poounah.shd8rzq.mongodb.net']
        query_string = 'retryWrites=true&w=majority'


        ## Connection String
        uri = "mongodb+srv://{0}:{1}@{2}/?{3}".format(
            user
            , password
            , cluster
            , query_string
        )
 
        client = pymongo.MongoClient(uri)
        db = client[os.environ['DB']]

        return client, db

        ##mongodb+srv://Frostito:<password>@poounah.shd8rzq.mongodb.net/?retryWrites=true&w=majority