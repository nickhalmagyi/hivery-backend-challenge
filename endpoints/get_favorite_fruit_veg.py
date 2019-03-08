from input_validations import ValidationError

from settings import PEOPLE_INDEX_COLNAME, PEOPLE_USERNAME_COLNAME, PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME, \
    PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME, FRUIT_VEG_KEYS, FRUIT_VEG_KEYS_MAP



class FruitVeg:
    def __init__(self, collection_people, person_index):
        self._validate_person_exists(collection_people, person_index)
        self.fruit_veg_keys = FRUIT_VEG_KEYS
        self.fruit_veg_keys_map = FRUIT_VEG_KEYS_MAP


    def _validate_person_exists(self, collection_people, person_index):
        if collection_people.count_documents({PEOPLE_INDEX_COLNAME: person_index}) == 0:
            raise ValidationError("The person_index {} does not exist.".format(person_index))


    def get_favorite_fruit_veg(self, collection_people, person_index):
        for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
            fruit_veg = {self.fruit_veg_keys_map[fruit_veg_key]:person[fruit_veg_key] for fruit_veg_key in self.fruit_veg_keys}
            return fruit_veg

