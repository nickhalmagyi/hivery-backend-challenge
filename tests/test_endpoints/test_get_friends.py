import unittest
from pymongo import MongoClient

from setup.mongo_init import load_data_to_mongo
from endpoints.get_friends import CommonFriends
from test_settings import *


friends_1 = [{'name': 'Decker Mckenzie', 'age': 60, 'address': '492 Stockton Street, Lawrence, Guam, 4854', 'phone': '+1 (893) 587-3311'}]

class TestCommonFriends(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient(HOST_NAME_TEST, PORT_NAME_TEST)
        self.db = self.client[DB_NAME_TEST]
        self.collection_companies = self.db[COMPANIES_COLLECTION_NAME_TEST]
        self.collection_people = self.db[PEOPLE_COLLECTION_NAME_TEST]
        self.person_index_1_test = 0
        self.person_index_2_test = 1
        self.common_friends_test = CommonFriends(self.collection_people,
                                              self.person_index_1_test,
                                              self.person_index_2_test)

    def test_get_friends_details(self):
        friends_details = self.common_friends_test.get_friends_details(self.collection_people,
                                              self.person_index_1_test,
                                              self.person_index_2_test)
        self.assertEqual(friends_details, friends_1)


if __name__ == '__main__':
    unittest.main()