import unittest
from pymongo import MongoClient
from setup.mongo_init import load_data_to_mongo

from test_settings import *


class TestMongoInit(unittest.TestCase):

    def setUp(self):
        load_data_to_mongo(db_name=DB_NAME_TEST,
                           companies_collection_name=COMPANIES_COLLECTION_NAME_TEST,
                           companies_json_path=COMPANIES_JSON_PATH_TEST,
                           people_collection_name=PEOPLE_COLLECTION_NAME_TEST,
                           people_json_path=PEOPLE_JSON_PATH_TEST)

        self.host_name = HOST_NAME_TEST
        self.port_name = PORT_NAME_TEST
        self.client = MongoClient(self.host_name, self.port_name)

    def test_db_exists(self):
        dbs = self.client.list_database_names()
        self.assertTrue(DB_NAME_TEST in dbs)


    def test_companies_collections_exists(self):
        db = self.client[DB_NAME_TEST]
        cols = db.list_collection_names()
        self.assertTrue(COMPANIES_COLLECTION_NAME_TEST in cols)

    def test_people_collections_exists(self):
        db = self.client[DB_NAME_TEST]
        cols = db.list_collection_names()
        self.assertTrue(PEOPLE_COLLECTION_NAME_TEST in cols)


if __name__ == '__main__':
    unittest.main()