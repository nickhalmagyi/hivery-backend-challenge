from pymongo import MongoClient
import os
import json

from settings import COMPANIES_JSON_PATH, PEOPLE_JSON_PATH, DB_NAME, HOST_NAME, PORT_NAME, \
    COMPANIES_COLLECTION_NAME, PEOPLE_COLLECTION_NAME, \
    FRUIT_LIST, VEG_LIST, \
    PEOPLE_FAVORITE_FOOD_COLNAME, PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME



def get_fruits(foods):
    return [food for food in foods if food in FRUIT_LIST]


def get_veg(foods):
    return [food for food in foods if food in VEG_LIST]


def init_collection(db, collection_name, collection_json_path):
    if db[collection_name]:
        db[collection_name].drop()

    with open(collection_json_path, 'r') as f:
        collection_json = json.load(f)

    collection = db[collection_name]
    print("Loading data into the mongodb.collection: {}.{}".format(db.name, collection_name))
    collection.insert_many(collection_json)


def process_food(collection_people):
    for person in collection_people.find():
        fruits = get_fruits(person[PEOPLE_FAVORITE_FOOD_COLNAME])
        vegs = get_veg(person[PEOPLE_FAVORITE_FOOD_COLNAME])
        collection_people.update_one({"_id": person["_id"]}, {"$set": {PEOPLE_FAVORITE_FRUIT_COLNAME: fruits}})
        collection_people.update_one({"_id": person["_id"]}, {"$set": {PEOPLE_FAVORITE_VEGETABLE_COLNAME: vegs}})


def load_data_to_mongo():
    client = MongoClient(HOST_NAME, PORT_NAME)
    db = client[DB_NAME]

    init_collection(db, COMPANIES_COLLECTION_NAME, COMPANIES_JSON_PATH)
    init_collection(db, PEOPLE_COLLECTION_NAME, PEOPLE_JSON_PATH)

    process_food(db[PEOPLE_COLLECTION_NAME])