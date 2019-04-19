from django.core.exceptions import ValidationError

"""
Methods used by Django as data validation before saving in the database


:param value: the value to test
:return: None, raise a ValidationError if the value isn't valid
"""


def validate_nonzero(value):
    """
    Validate if the field is greater than 0

    :param value: the value to test
    :return: None, raise a ValidationError if the value isn't valid
    """
    if value <= 0:
        raise ValidationError(
            message="%(value)s is not greater than 0",
            params={'value': value},
        )


def validate_isbn10(value: str):
    """
    Validate if the value is a valid ISBN10


    :param value: the value to test
    :return: None, raise a ValidationError if the value isn't valid
    """
    if len(value) != 10 or not value.isdigit():
        raise ValidationError(
            message='%(value)s is not a valid ISBN 10',
            params={'value': value},
        )


def validate_isbn13(value: str):
    """
    Validate if the value is a valid ISBN13

    :param value: the value to test
    :return: None, raise a ValidationError if the value isn't valid
    """
    if not (len(value) == 13 and
            (value.startswith("979") or value.startswith("978")) and
            value.isdigit()):
        raise ValidationError(
            message='%(value)s is not a valid ISBN 13',
            params={'value': value},
        )