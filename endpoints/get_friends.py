from endpoints.input_validations import ValidationError

from settings import PEOPLE_FRIENDS_COLNAME, PEOPLE_NAME_COLNAME, \
    PEOPLE_INDEX_COLNAME, FRIENDS_INDEX_COLNAME, PEOPLE_EYECOLOR_COLNAME, BROWN_EYECOLOR, \
    PEOPLE_HAS_DIED_COLNAME, PEOPLE_AGE_COLNAME, PEOPLE_ADDRESS_COLNAME, PEOPLE_PHONE_COLNAME


class CommonFriends:
    def __init__(self, collection_people, person_index_1, person_index_2):
        self._validate_person_index_exists(collection_people, person_index_1)
        self._validate_person_index_exists(collection_people, person_index_2)


    def _validate_person_index_exists(self, collection_people, person_index):
        if collection_people.count_documents({PEOPLE_INDEX_COLNAME: person_index}) == 0:
            raise ValidationError("The person_index {} does not exist.".format(person_index))


    def _get_common_friends(self, collection_people, person_index_1, person_index_2):
        query = {
            PEOPLE_INDEX_COLNAME: {'$in': [person_index_1, person_index_2]},
        }
        common_friends_indices = set()
        for person in collection_people.find(query):
            friends = {friend[FRIENDS_INDEX_COLNAME] for friend in person[PEOPLE_FRIENDS_COLNAME]}
            common_friends_indices = common_friends_indices.union(friends)
        return list(common_friends_indices)


    def get_friends_details(self, collection_people, person_index_1, person_index_2):
        common_friends_indices = self._get_common_friends(collection_people, person_index_1, person_index_2)

        query = {
            PEOPLE_INDEX_COLNAME: {'$in': common_friends_indices},
            PEOPLE_EYECOLOR_COLNAME: BROWN_EYECOLOR,
            PEOPLE_HAS_DIED_COLNAME: False
        }

        attributes_list = [PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME, PEOPLE_ADDRESS_COLNAME,
                           PEOPLE_PHONE_COLNAME, PEOPLE_EYECOLOR_COLNAME, PEOPLE_HAS_DIED_COLNAME]

        friends = []
        for person in collection_people.find(query):
            person_attributes = {attribute: person[attribute] for attribute in attributes_list}
            friends.append(person_attributes)
        return friends

