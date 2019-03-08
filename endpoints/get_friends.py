from endpoints.validations import validate_index

from settings import PEOPLE_FRIENDS_COLNAME, PEOPLE_NAME_COLNAME, \
    PEOPLE_INDEX_COLNAME, FRIENDS_INDEX_COLNAME, PEOPLE_EYECOLOR_COLNAME, BROWN_EYECOLOR, \
    PEOPLE_HAS_DIED_COLNAME, PEOPLE_AGE_COLNAME, PEOPLE_ADDRESS_COLNAME, PEOPLE_PHONE_COLNAME


def get_friends(collection_people, person_index):
    person_index = validate_index(person_index)
    for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
        friends = [friend[FRIENDS_INDEX_COLNAME] for friend in person[PEOPLE_FRIENDS_COLNAME]]
        return friends
    return []


def get_common_friends(collection_people, person_index_1, person_index_2):
    friends_1 = get_friends(collection_people, person_index_1)
    friends_2 = get_friends(collection_people, person_index_2)
    common_friends_indices = list(set(friends_1).intersection(friends_2))
    return common_friends_indices


def person_has_brown_eyes(collection_people, person_index):
    for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
        eyecolor = person[PEOPLE_EYECOLOR_COLNAME]
    return eyecolor == BROWN_EYECOLOR


def person_is_alive(collection_people, person_index):
    for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
        has_died = person[PEOPLE_HAS_DIED_COLNAME]
    return has_died == False


def person_has_brown_eyes_and_is_alive(collection_people, person_index):
    brown_eyes = person_has_brown_eyes(collection_people, person_index)
    is_alive = person_is_alive(collection_people, person_index)
    if brown_eyes and is_alive:
        return True
    return False


def get_name_age_address_phone(collection_people, person_index):
    for person in collection_people.find({PEOPLE_INDEX_COLNAME: person_index}):
        attributes = [PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME, PEOPLE_ADDRESS_COLNAME, PEOPLE_PHONE_COLNAME]
        person = {attribute: person[attribute] for attribute in attributes}
    return person