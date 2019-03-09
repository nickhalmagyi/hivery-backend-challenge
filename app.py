import os
import json
from flask import Flask, request
from pymongo import MongoClient

from input_validations import GetEmployeesForm, GetFriendsForm, GetFruitVegForm
from endpoints.get_employees import Employees
from endpoints.get_friends import CommonFriends
from endpoints.get_favorite_fruit_veg import FruitVeg
from settings import DEBUG, HOST_NAME, PORT_NAME, DB_NAME, COMPANIES_COLLECTION_NAME, PEOPLE_COLLECTION_NAME


def create_app():
    app = Flask(__name__)

    client = MongoClient(HOST_NAME, PORT_NAME)
    db = client[DB_NAME]
    collection_companies = db[COMPANIES_COLLECTION_NAME]
    collection_people = db[PEOPLE_COLLECTION_NAME]


    @app.route('/get_employees', methods=['GET'])
    def get_employees():
        """
        :return: all employees of a given company
        """
        form = GetEmployeesForm(request.args)
        if not form.validate():
            errors = {'errors': True}
            errors.update(form.errors)
            return json.dumps(errors)
        company_index = form.data.get('company_index')

        employees = Employees(collection_companies, company_index)
        if employees.errors != []:
            return json.dumps(employees.errors)
        employees = employees.get_all_employees(collection_companies, collection_people, company_index)
        return json.dumps(employees)


    @app.route('/get_friends', methods=['GET'])
    def get_friends():
        """
        :return: common friends between person_index_1 and person_index_2, who are alive and brown-eyed.
        """
        form = GetFriendsForm(request.args)
        if not form.validate():
            errors = {'errors': True}
            errors.update(form.errors)
            return json.dumps(errors)
        person_index_1 = form.data.get('person_index_1')
        person_index_2 = form.data.get('person_index_2')

        common_friends = CommonFriends(collection_people, person_index_1, person_index_2)
        if common_friends.errors != []:
            return json.dumps(common_friends.errors)

        friends_details = common_friends.get_friends_details(collection_people, person_index_1, person_index_2)
        return json.dumps(friends_details)


    @app.route('/get_fruit_veg', methods=['GET'])
    def get_fruit_veg():
        """
        :return: name, age, favorite fruits and vegetables of person_index
        """
        form = GetFruitVegForm(request.args)
        if not form.validate():
            errors = {'errors': True}
            errors.update(form.errors)
            return json.dumps(errors)
        person_index = form.data.get('person_index')

        fruit_veg = FruitVeg(collection_people, person_index)
        if fruit_veg.errors != []:
            return json.dumps(fruit_veg.errors)
        favorite_fruit_veg = fruit_veg.get_favorite_fruit_veg(collection_people, person_index)
        return json.dumps(favorite_fruit_veg)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG)
