class ValidationError(Exception):
    pass


def validate_integer_index(index):
    try:
        index = int(index)
    except ValueError:
        raise ValidationError("Input must be an integer")
    else:
        return index
