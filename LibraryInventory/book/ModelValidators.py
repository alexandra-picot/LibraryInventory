from django.core.exceptions import ValidationError


def validate_nonzero(value):
    """
    Method used by Django as data validation before saving in the database

    :param value: the value to test
    :return: None, raise a ValidationError if the value isn't valid
    """
    if value <= 0:
        raise ValidationError(
            message="%(value)s is not greater than 0",
            params={'value': value},
        )