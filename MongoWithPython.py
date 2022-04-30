import pymongo
from urllib.parse import quote, quote_plus

mongo_uri = "mongodb+srv://shopuser:" + quote_plus("userpassword") + "@cluster0.tk0m2.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

print(mongo_uri)

client = pymongo.MongoClient(mongo_uri)

documents = [
        {
            "sku":"111445001",
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
            "sku":"111445002",
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
            "sku":"111445003",
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
    print(do_insert.inserted_ids)

#insertMany(client,documents)


def readDocuments(client, condition):
    db = client["PythonDB"]
    col = db["dummyCollection"]
    results = col.find(condition)
    # db.collectio.find({})

    for row in results:
        print(row)