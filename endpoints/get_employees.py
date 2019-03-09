from settings import COMPANY_NAME_COLNAME, COMPANY_INDEX_COLNAME, PEOPLE_COMPANYID_COLNAME


class Employees:
    def __init__(self, collection_companies, company_index):
        self.errors = {"errors": False}
        self._validate_company_exists("company_index", collection_companies, company_index, COMPANY_INDEX_COLNAME)


    def _validate_company_exists(self, index_name, collection, index, index_colname):
        if collection.count_documents({index_colname: index}) == 0:
            self.errors["errors"] = True
            self.errors.update({index_name : ["The index {} was not found.".format(index)]})

    def _get_company(self, collection_companies, company_index):

        company = collection_companies.find({COMPANY_INDEX_COLNAME: company_index})

        for comp in company:
            return {PEOPLE_COMPANYID_COLNAME: comp[COMPANY_INDEX_COLNAME]}

    def get_all_employees(self, collection_companies, collection_people, company_index):

        company = self._get_company(collection_companies, company_index)
        employees = []
        for person in collection_people.find(company):
            employees.append(person)
        employees = [{'employee_count': len(employees)}] + employees

        return employees
