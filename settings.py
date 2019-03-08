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
COMPANY_INDEX_COLNNAME = "index"

COMPANY_ID_COLNAME = "company_id"
