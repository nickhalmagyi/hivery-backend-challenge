from pymongo import MongoClient
import os
import json

from settings import COMPANIES_JSON_PATH, PEOPLE_JSON_PATH, DB_NAME, COMPANIES_COLLECTION_NAME, PEOPLE_COLLECTION_NAME


def init_collection(db, collection_name, collection_json_path):
    if db[collection_name]:
        db[collection_name].drop()

    with open(collection_json_path, 'r') as f:
        collection_json = json.load(f)

    collection = db[collection_name]
    print("Loading data into the mongodb.collection: {}.{}".format(db.name, collection_name))
    collection.insert_many(collection_json)


def load_data_to_mongo():
    client = MongoClient('localhost', 27017)
    db = client[DB_NAME]

    init_collection(db, COMPANIES_COLLECTION_NAME, COMPANIES_JSON_PATH)
    init_collection(db, PEOPLE_COLLECTION_NAME, PEOPLE_JSON_PATH)