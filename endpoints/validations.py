from settings import COMPANY_INDEX_COLNAME, PEOPLE_INDEX_COLNAME

def validate_person_index(collection_people, index):
    index = validate_integer_index(index)
    index = person_index_exists(collection_people, index)
    return index


def validate_company_index(collection_companies, index):
    index = validate_integer_index(index)
    index = company_index_exists(collection_companies, index)
    return index


def validate_integer_index(index):
    try:
        index = int(index)
    except ValueError:
        raise ValueError("Input must be an integer")
    return index


def person_index_exists(collection_people, person_index):
    if collection_people.count_documents({PEOPLE_INDEX_COLNAME: person_index})==0:
        raise ValueError('No record of person_index = {}'.format(person_index))
    return person_index


def company_index_exists(collection_companies, company_index):
    if collection_companies.count_documents({COMPANY_INDEX_COLNAME: company_index})==0:
        raise ValueError('No record of company_index = {}'.format(company_index))
    return company_index
