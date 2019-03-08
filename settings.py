import os

DEBUG = True

DATA_DIR = "resources"

DB_NAME = 'hivery'
HOST_NAME = 'localhost'
PORT_NAME = 27017

# The mongodb name of the "companies" and "people" collection
COMPANIES_COLLECTION_NAME = "companies"
PEOPLE_COLLECTION_NAME = "people"

COMPANIES_JSON_FNAME = "companies.json"
COMPANIES_JSON_PATH = os.path.join(DATA_DIR, COMPANIES_JSON_FNAME)

PEOPLE_JSON_FNAME = "people.json"
PEOPLE_JSON_PATH = os.path.join(DATA_DIR, PEOPLE_JSON_FNAME)

COMPANY_NAME_COLNAME = "company"
COMPANY_INDEX_COLNAME = "index"
COMPANY_ID_COLNAME = "company_id"

PEOPLE_FRIENDS_COLNAME = 'friends'
PEOPLE_NAME_COLNAME = 'name'
PEOPLE_AGE_COLNAME = 'age'
PEOPLE_ADDRESS_COLNAME = 'address'
PEOPLE_PHONE_COLNAME = "phone"
PEOPLE_INDEX_COLNAME = 'index'
PEOPLE_EYECOLOR_COLNAME = 'eyeColor'
PEOPLE_HAS_DIED_COLNAME = "has_died"
PEOPLE_FAVORITE_FOOD_COLNAME = "favouriteFood"
PEOPLE_FAVORITE_FRUIT_COLNAME = "fruits"
PEOPLE_FAVORITE_VEGETABLE_COLNAME = "vegetables"

FRIENDS_INDEX_COLNAME = 'index'

BROWN_EYECOLOR = "brown"

FRUIT_LIST = ['apple', 'banana', 'orange', 'strawberry']
VEG_LIST = ['beetroot', 'carrot', 'celery', 'cucumber']

PEOPLE_USERNAME_COLNAME = 'username'
