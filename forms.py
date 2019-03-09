from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange, Optional


def validate_index(index):
    return [InputRequired(message="You must enter a value for {}.".format(index))]


class GetEmployeesForm(Form):
    company_index = IntegerField('company_index', validators=validate_index('company_index'))


class GetFriendsForm(Form):
    person_index_1 = IntegerField('person_index_1', validators=validate_index('person_index_1'))
    person_index_2 = IntegerField('person_index_2', validators=validate_index('person_index_2'))


class GetFruitVegForm(Form):
    person_index = IntegerField('person_index_1', validators=validate_index('person_index'))

