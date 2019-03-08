import unittest
from pymongo import MongoClient

from setup.mongo_init import load_data_to_mongo
from endpoints.get_employees import Employees
from test_settings import *


employee_1 = [{'employee_count': 1}, {'_id': '595eeb9b96d80a5bc7afb106', 'index': 0, 'has_died': True, 'age': 61, 'eyeColor': 'blue', 'name': 'Carmella Lambert', 'company_id': 0, 'email': 'carmellalambert@earthmark.com', 'phone': '+1 (910) 567-3630', 'address': '628 Sumner Place, Sperryville, American Samoa, 9819', 'friends': [{'index': 0}, {'index': 1}, {'index': 2}], 'favouriteFood': ['orange', 'apple', 'banana', 'strawberry'], 'fruits': ['orange', 'apple', 'banana', 'strawberry'], 'vegetables': []}]

class TestEmployees(unittest.TestCase):

    def setUp(self):
        self.client = MongoClient(HOST_NAME_TEST, PORT_NAME_TEST)
        self.db = self.client[DB_NAME_TEST]
        self.collection_companies = self.db[COMPANIES_COLLECTION_NAME_TEST]
        self.collection_people = self.db[PEOPLE_COLLECTION_NAME_TEST]
        self.company_index_test = 0
        self.employees_test = Employees(self.collection_companies, self.company_index_test)

    def test_get_all_employees(self):
        employees = self.employees_test.get_all_employees(self.collection_companies,
                                              self.collection_people,
                                              self.company_index_test)
        self.assertEqual(employees, employee_1)


if __name__ == '__main__':
    unittest.main()