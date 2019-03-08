from settings import COMPANY_NAME_COLNAME, COMPANY_INDEX_COLNAME, PEOPLE_COMPANYID_COLNAME
from endpoints.input_validations import ValidationError


class Employees:
    def __init__(self, collection_companies, company_index):
        self._validate_company_exists(collection_companies, company_index)

    def _validate_company_exists(self, collection_companies, company_index):
        if collection_companies.count_documents({COMPANY_INDEX_COLNAME: company_index}) == 0:
            raise ValidationError("The company_index {} does not exist.".format(company_index))


    def _get_company(self, collection_companies, company_index):

        company = collection_companies.find({COMPANY_INDEX_COLNAME: company_index})

        for comp in company:
            return {PEOPLE_COMPANYID_COLNAME: comp[COMPANY_INDEX_COLNAME]}

    def get_all_employees(self, collection_companies, collection_people, company_index):

        company = self._get_company(collection_companies, company_index)

        employees = []
        for person in collection_people.find(company):
            print(person['name'], ": ", person[PEOPLE_COMPANYID_COLNAME])
            employees.append(person)
        employees = [{'employee_count': len(employees)}] + employees

        return employees
