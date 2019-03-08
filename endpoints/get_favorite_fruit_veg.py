from endpoints.input_validations import ValidationError

from settings import PEOPLE_INDEX_COLNAME, PEOPLE_USERNAME_COLNAME, PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME, \
    PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME


FOODS = [PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME,
                 PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME]

FOODS_OUT = [PEOPLE_USERNAME_COLNAME, PEOPLE_AGE_COLNAME,
                     PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME]


class FruitVeg:
    def __init__(self, collection_people, person_index):
        self._validate_person_exists(collection_people, person_index)
        self.foods = FOODS
        self.foods_out = FOODS_OUT
        self.food_map = self._make_food_map(self.foods, self.foods_out)

    def _validate_person_exists(self, collection_people, person_index):
        if collection_people.count_documents({PEOPLE_INDEX_COLNAME: person_index}) == 0:
            raise ValidationError("The person_index {} does not exist.".format(person_index))

    def _make_food_map(self, foods, foods_out):
        """
        For some odd reason we are required to map the key "name" to "username"
        :return: a dict which converts "name" to "username"
        """
        food_map = dict(zip(foods, foods_out))

        return food_map

    def get_favorite_fruit_veg(self, collection_people, person_index):
        for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
            food_out = {self.food_map[food]:person[food] for food in self.foods}
            return food_out

