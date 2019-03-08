from settings import COMPANY_NAME_COLNAME, COMPANY_INDEX_COLNAME, COMPANY_ID_COLNAME


def get_company(collection_companies, company_index):
    company = collection_companies.find({COMPANY_INDEX_COLNAME: company_index})
    if company:
        for comp in company:
            return {COMPANY_ID_COLNAME: comp[COMPANY_INDEX_COLNAME]}
        else:
            return {'Error': 'Company name {} does not exist.'.format(company_name)}


def get_all_employees(collection_companies, collection_people, company_name):

    company = get_company(collection_companies, company_name)
    if 'Error' in company.keys():
        return [company]

    employees = []
    for person in collection_people.find(company):
        print(person['name'], ": ", person[COMPANY_ID_COLNAME])
        employees.append(person)
    employees = [{'employee_count': len(employees)}] + employees

    return employees