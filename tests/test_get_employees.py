import unittest
from setup.mongo_init import load_data_to_mongo

from test_settings import *


class TestIsNullOrEmpty(unittest.TestCase):

    def setUp(self):
        load_data_to_mongo(db_name=DB_NAME_TEST,
                           companies_collection_name=COMPANIES_COLLECTION_NAME_TEST,
                           companies_json_path=COMPANIES_JSON_PATH_TEST,
                           people_collection_name=PEOPLE_COLLECTION_NAME_TEST,
                           people_json_path=PEOPLE_JSON_PATH_TEST)



if __name__ == '__main__':
    unittest.main()