import os
import json
from flask import Flask, request
from pymongo import MongoClient

from endpoints.get_employees import Employees
from endpoints.get_friends import CommonFriends
from endpoints.get_favorite_fruit_veg import FruitVeg
from endpoints.input_validations import validate_integer_index
from settings import DEBUG, HOST_NAME, PORT_NAME, DB_NAME, COMPANIES_COLLECTION_NAME, PEOPLE_COLLECTION_NAME


def create_app():
    app = Flask(__name__)

    client = MongoClient(HOST_NAME, PORT_NAME)
    db = client[DB_NAME]
    collection_companies = db[COMPANIES_COLLECTION_NAME]
    collection_people = db[PEOPLE_COLLECTION_NAME]


    @app.route('/get_employees', methods=['GET'])
    def get_employees():
        company_index = request.args.get('company_index')
        company_index = validate_integer_index(company_index)

        employees = Employees(collection_companies, company_index)

        employees = employees.get_all_employees(collection_companies, collection_people, company_index)
        return json.dumps(employees)


    @app.route('/get_friends', methods=['GET'])
    def get_friends():
        person_index_1 = validate_integer_index(request.args.get('person_index_1'))
        person_index_2 = validate_integer_index(request.args.get('person_index_2'))
        common_friends = CommonFriends(collection_people, person_index_1, person_index_2)
        friends_details = common_friends.get_friends_details(collection_people, person_index_1, person_index_2)
        return json.dumps(friends_details)


    @app.route('/get_fruit_veg', methods=['GET'])
    def get_fruits():
        person_index = validate_integer_index(request.args.get('person_index'))
        fruit_veg = FruitVeg(collection_people, person_index)
        favorite_fruit_veg = fruit_veg.get_favorite_fruit_veg(collection_people, person_index)
        return json.dumps(favorite_fruit_veg)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG)
