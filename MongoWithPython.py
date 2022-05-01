import pymongo
from urllib.parse import quote, quote_plus
import certifi
ca = certifi.where()

mongo_uri = "mongodb+srv://shopuser:" + quote_plus("userpassword") + "@cluster0.tk0m2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"


client = pymongo.MongoClient(f"mongodb+srv://shopuser:" + quote_plus("userpassword") + "@cluster0.tk0m2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority", tlsCAFile=ca)



documents = [
        {
            "sku":"111445007",
            "title":"Simsong One mobile phone",
            "description":"The greatest Onedroid phone on the market .....",
            "weight":350,
            "width":10,
            "height":10,
            "depth":1,
            "quantity":99,
            "price":1000,
        },
        {
            "sku":"111445008",
            "title":"Simsong One mobile phone",
            "description":"The greatest Onedroid phone on the market .....",
            "weight":350,
            "width":10,
            "height":10,
            "depth":1,
            "quantity":99,
            "price":1000,
        },
        {
            "sku":"111445009",
            "title":"Simsong One mobile phone",
            "description":"The greatest Onedroid phone on the market .....",
            "weight":350,
            "width":10,
            "height":10,
            "depth":1,
            "quantity":99,
            "price":1000,
        },
        {
            "sku":"111445004",
            "title":"Simsong One mobile phone",
            "description":"The greatest Onedroid phone on the market .....",
            "weight":350,
            "width":10,
            "height":10,
            "depth":1,
            "quantity":99,
            "price":1000,
        },
    ]


def insertMany(client, documents):
    db = client["PythonDB"]
    collection = db["products"]
    do_insert = collection.insert_many(documents)
    # print(do_insert.inserted_ids)

#insertMany(client,documents)


def readDocs(client, condition):
    db = client["PythonDB"]
    collection = db["products"]
    results = collection.find(condition)

    for row in results:
        print(row)


#readDocs(client,{"title": "Simsong One mobile phone"})
#readDocs(client,{'sku': '111445008'})
readDocs(client,{})  # SELECT * FROM products

