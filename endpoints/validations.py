from settings import PEOPLE_INDEX_COLNAME

def validate_index(collection_people, person_index):
    person_index = validate_integer_index(person_index)
    person_index = person_index_exists(collection_people, person_index)
    return person_index


def validate_integer_index(person_index):
    try:
        person_index = int(person_index)
    except ValueError:
        raise ValueError("Input must be an integer")
    return person_index


def person_index_exists(collection_people, person_index):
    if collection_people.count_documents({PEOPLE_INDEX_COLNAME: person_index})==0:
        raise ValueError('No record of person_index = {}'.format(person_index))
    return person_index