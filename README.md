# Setup

In addition to Mongodb and Python3, the Dependencies are in setup/requirements.txt.
Running
python3 setup.py
will update pip, install python dependencies and load the data into mongodb.
In addition it will perform some preprocessing on the database, adding field "fruits" and "vegetables".

The default parameters for mongodb are in settings.py and are the standard hostname and port.

The db name is set to "hivery".

Only the files in resources named companies.json and people.json are loaded into mongodb, as collections.

# Endpoints

Examples of the three endpoints are as follows:

http://127.0.0.1:5000/get_employees?company_index=1
http://127.0.0.1:5000/get_friends?person_index_1=5&person_index_2=2
http://127.0.0.1:5000/get_fruit_veg?person_index=7  

They all use company/person indices are the parameters, which have been checked to be unique. New files
uploaded should also have unique indices for both companies and people.

If the value of an argument in the query string is non-integer or is not found in the db, a ValueError is thrown.

The endpoint get_employees contains a field "employee_count" which serves as a check on the number of employees
returned in json format. When there are no employees in the given company, one will find the output

[{"employee_count": 0}]


