from settings import PEOPLE_INDEX_COLNAME, PEOPLE_USERNAME_COLNAME, PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME, \
    PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME

def get_favorite_fruit_veg(collection_people, person_index):

    for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
        print(person)

        # For some reasons we are required to map the key "name" to "username"
        FOODS = [PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME,
                 PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME]
        FOODS_OUT = [PEOPLE_USERNAME_COLNAME, PEOPLE_AGE_COLNAME,
                 PEOPLE_FAVORITE_FRUIT_COLNAME, PEOPLE_FAVORITE_VEGETABLE_COLNAME]
        food_map = dict(zip(FOODS, FOODS_OUT))

        food_out = {food_map[food]:person[food] for food in FOODS}

        return food_out

