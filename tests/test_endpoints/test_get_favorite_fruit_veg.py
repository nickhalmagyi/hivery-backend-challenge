import unittest
from pymongo import MongoClient

from setup.mongo_init import load_data_to_mongo
from endpoints.get_favorite_fruit_veg import FruitVeg
from test_settings import *


favorite_fruit_veg_1 = {'username': 'Carmella Lambert', 'age': 61, 'fruits': ['orange', 'apple', 'banana', 'strawberry'], 'vegetables': []}

class TestFruitVeg(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient(HOST_NAME_TEST, PORT_NAME_TEST)
        self.db = self.client[DB_NAME_TEST]
        self.collection_companies = self.db[COMPANIES_COLLECTION_NAME_TEST]
        self.collection_people = self.db[PEOPLE_COLLECTION_NAME_TEST]
        self.person_index_test = 0
        self.fruit_veg_test = FruitVeg(self.collection_people,
                                              self.person_index_test)
        print()

    def test_get_friends_details(self):
        favorite_fruit_veg = self.fruit_veg_test.get_favorite_fruit_veg(self.collection_people,
                                              self.person_index_test)
        self.assertEqual(favorite_fruit_veg, favorite_fruit_veg_1)


if __name__ == '__main__':
    unittest.main()