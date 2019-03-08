import unittest
from setup.mongo_init import load_data_to_mongo

from settings import


class TestIsNullOrEmpty(unittest.TestCase):

    def setUp(self):
        load_data_to_mongo()
        load_data_to_mongo(db_name=DB_NAME,
                           companies_collection_name=COMPANIES_COLLECTION_NAME,
                           companies_json_path=COMPANIES_JSON_PATH,
                           people_collection_name=PEOPLE_COLLECTION_NAME,
                           people_json_path=PEOPLE_JSON_PATH):

    def test_None(self):
        self.assertEqual(isNullOrEmpty(None), True)

    def test_Empty(self):
        self.assertEqual(isNullOrEmpty(""), True)

    def test_NotEmpty(self):
        self.assertEqual(isNullOrEmpty("a"), False)

    def test_edgecase_1(self):
        self.assertEqual(isNullOrEmpty("None"), False)

    def test_edgecase_2(self):
        self.assertEqual(isNullOrEmpty(" "), False)


if __name__ == '__main__':
    unittest.main()