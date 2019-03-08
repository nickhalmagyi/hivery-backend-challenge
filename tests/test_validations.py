import unittest
from input_validations import validate_integer_index, ValidationError


class TestValidations(unittest.TestCase):

    def setUp(self):
        pass

    def test_validate_integer_index_1(self):
        self.assertRaises(ValidationError, validate_integer_index, 'x')


    def test_validate_integer_index_3(self):
        self.assertEqual(validate_integer_index(17), 17)

if __name__ == '__main__':
    unittest.main()