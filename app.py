import os
import json
from flask import Flask, request
from pymongo import MongoClient
from endpoints.get_employees import get_all_employees

from settings import DEBUG, HOST_NAME, PORT_NAME, DB_NAME, COMPANIES_COLLECTION_NAME, PEOPLE_COLLECTION_NAME


def create_app():
    app = Flask(__name__)

    client = MongoClient(HOST_NAME, PORT_NAME)
    db = client[DB_NAME]
    col_companies = db[COMPANIES_COLLECTION_NAME]
    col_people = db[PEOPLE_COLLECTION_NAME]


    @app.route('/', methods=['GET'])
    def index():
        return json.dumps("Hello World!")


    @app.route('/get_employees', methods=['GET'])
    def get_employees():
        company_name = request.args.get('company_name').upper()
        employees = get_all_employees(col_companies, col_people, company_name)
        return json.dumps(employees)

    @app.route('/get_friends', methods=['GET'])
    def get_friends():
        friend_1 = request.args.get('friend_1')
        friend_2 = request.args.get('friend_2')

        return json.dumps([friend_1, friend_2])

    @app.route('/get_fruits', methods=['GET'])
    def get_fruits():
        person = request.args.get('person')
        return json.dumps(person)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=DEBUG)
