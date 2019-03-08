from settings import COMPANY_NAME_COLNAME, COMPANY_INDEX_COLNNAME, COMPANY_ID_COLNAME


def get_company(col_companies, company_name):
    company = col_companies.find({COMPANY_NAME_COLNAME: company_name})
    if company:
        for comp in company:
            return {COMPANY_ID_COLNAME: comp[COMPANY_INDEX_COLNNAME]}
        else:
            return {'Error': 'Company name {} does not exist.'.format(company_name)}


def get_all_employees(col_companies, col_people, company_name):

    company = get_company(col_companies, company_name)
    if 'Error' in company.keys():
        return [company]

    employees = []
    for person in col_people.find(company):
        print(person['name'], ": ", person[COMPANY_ID_COLNAME])
        employees.append(person)
    employees = [{'employee_count': len(employees)}] + employees

    return employees