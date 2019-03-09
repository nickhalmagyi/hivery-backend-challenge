# from input_validations import ValidationError

from settings import PEOPLE_FRIENDS_COLNAME, PEOPLE_NAME_COLNAME, \
    PEOPLE_INDEX_COLNAME, FRIENDS_INDEX_COLNAME, PEOPLE_EYECOLOR_COLNAME, BROWN_EYECOLOR, \
    PEOPLE_HAS_DIED_COLNAME, PEOPLE_AGE_COLNAME, PEOPLE_ADDRESS_COLNAME, PEOPLE_PHONE_COLNAME


class CommonFriends:
    def __init__(self, collection_people, person_index_1, person_index_2):
        self.errors = {"errors": False}
        self._validate_person_index_exists("person_index_1", collection_people, person_index_1, PEOPLE_INDEX_COLNAME)
        self._validate_person_index_exists("person_index_2", collection_people, person_index_2, PEOPLE_INDEX_COLNAME)


    def _validate_person_index_exists(self, index_name, collection, index, index_colname):
        if collection.count_documents({index_colname: index}) == 0:
            self.errors["errors"] = True
            self.errors.update({index_name : ["The index {} was not found.".format(index)]})


    def _get_common_friends(self, collection_people, person_index_1, person_index_2):
        """
        :param collection_people: mongodb collection
        :param person_index_1:  integer, the index of an entry in the peoples collection
        :param person_index_2:  integer, the index of an entry in the peoples collection
        :return: list of indices for the friends in common between person_index_1, person_index_2
        """
        query = {
            PEOPLE_INDEX_COLNAME: {'$in': [person_index_1, person_index_2]},
        }
        common_friends_indices = set()
        for person in collection_people.find(query):
            friends = {friend[FRIENDS_INDEX_COLNAME] for friend in person[PEOPLE_FRIENDS_COLNAME]}
            common_friends_indices = common_friends_indices.union(friends)
        return list(common_friends_indices)


    def get_friends_details(self, collection_people, person_index_1, person_index_2):
        """
        :param collection_people: mongodb collection
        :param person_index_1:  integer, the index of an entry in the peoples collection
        :param person_index_2:  integer, the index of an entry in the peoples collection
        :return: details of friends common to both person_index_1, person_index_2, who are alive and have brown eyes.
        """
        common_friends_indices = self._get_common_friends(collection_people, person_index_1, person_index_2)

        query = {
            PEOPLE_INDEX_COLNAME: {'$in': common_friends_indices},
            PEOPLE_EYECOLOR_COLNAME: BROWN_EYECOLOR,
            PEOPLE_HAS_DIED_COLNAME: False
        }

        attributes_list = [PEOPLE_NAME_COLNAME, PEOPLE_AGE_COLNAME, PEOPLE_ADDRESS_COLNAME,
                           PEOPLE_PHONE_COLNAME]

        friends = []
        for person in collection_people.find(query):
            person_attributes = {attribute: person[attribute] for attribute in attributes_list}
            friends.append(person_attributes)
        return friends

