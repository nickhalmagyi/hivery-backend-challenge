import os
import json
from flask import Flask, request
from pymongo import MongoClient
from endpoints.get_employees import get_all_employees
from endpoints.get_friends import get_common_friends, person_has_brown_eyes_and_is_alive, get_name_age_address_phone
from endpoints.get_favorite_fruit_veg import get_favorite_fruit_veg
from endpoints.validations import validate_index
from settings import DEBUG, HOST_NAME, PORT_NAME, DB_NAME, COMPANIES_COLLECTION_NAME, PEOPLE_COLLECTION_NAME


def create_app():
    app = Flask(__name__)

    client = MongoClient(HOST_NAME, PORT_NAME)
    db = client[DB_NAME]
    collection_companies = db[COMPANIES_COLLECTION_NAME]
    collection_people = db[PEOPLE_COLLECTION_NAME]


    @app.route('/', methods=['GET'])
    def index():
        return json.dumps("Hello World!")


    @app.route('/get_employees', methods=['GET'])
    def get_employees():
        company_name = request.args.get('company_name').upper()
        employees = get_all_employees(collection_companies, collection_people, company_name)
        return json.dumps(employees)


    @app.route('/get_friends', methods=['GET'])
    def get_friends():
        person_index_1 = validate_index(collection_people, request.args.get('person_index_1'))
        person_index_2 = validate_index(collection_people, request.args.get('person_index_2'))

        common_friends_indices = get_common_friends(collection_people, person_index_1, person_index_2)
        common_friends_with_brown_eyes_and_is_alive = [friend for friend in common_friends_indices
                                           if person_has_brown_eyes_and_is_alive(collection_people, friend)]
        friends = [get_name_age_address_phone(collection_people, friend)
                                                       for friend in common_friends_with_brown_eyes_and_is_alive]
        return json.dumps(friends)

    @app.route('/get_fruit_veg', methods=['GET'])
    def get_fruits():
        person_index = validate_index(collection_people, request.args.get('person_index'))
        fave_fruit_veg = get_favorite_fruit_veg(collection_people, person_index)
        return json.dumps(fave_fruit_veg)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG)
