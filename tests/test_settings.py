import os

DEBUG = True

DATA_DIR_TEST = "tests/resources"

DB_NAME_TEST = 'hivery_test'
HOST_NAME_TEST  = 'localhost'
PORT_NAME_TEST  = 27017

# The mongodb name of the "companies" and "people" collection
COMPANIES_COLLECTION_NAME_TEST  = "companies_test"
PEOPLE_COLLECTION_NAME_TEST  = "people_test"

COMPANIES_JSON_FNAME_TEST = "companies_test.json"
COMPANIES_JSON_PATH_TEST = os.path.join(DATA_DIR_TEST, COMPANIES_JSON_FNAME_TEST)

PEOPLE_JSON_FNAME_TEST = "people_test.json"
PEOPLE_JSON_PATH_TEST = os.path.join(DATA_DIR_TEST, PEOPLE_JSON_FNAME_TEST)

COMPANY_NAME_COLNAME = "company"
COMPANY_INDEX_COLNAME = "index"

PEOPLE_COMPANYID_COLNAME = "company_id"

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
