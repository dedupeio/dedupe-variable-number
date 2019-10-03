import re

from dedupe.variables.base import FieldType
from dedupe.variables.price import PriceType
import dedupe.predicates

def non_digit_strip(field):
    c_field = re.sub(r'^[^1234567890\-+.]+', '', field)
    return re.sub(r'[^1234567890.]+$', '', c_field)

def orderOfMagnitude(field):
    try:
        return dedupe.predicates.orderOfMagnitude(float(field.strip()))
    except ValueError:
        return ()

def roundTo1(field):
    try:
        return dedupe.predicates.roundTo1(float(field.strip()))
    except ValueError:
        return ()

class PositiveNumberType(FieldType):
    type = "PositiveNumber"

    def __init__(self, definition):
        super().__init__(definition)
        # always want to have a missing indicator to
        # handle the time we can't cast to positive number
        self.has_missing = True

    _predicate_functions = [dedupe.predicates.wholeFieldPredicate,
                            orderOfMagnitude,
                            roundTo1]


    @staticmethod
    def comparator(num_str_1, num_str_2):
        try:
            num_1 = float(non_digit_strip(num_str_1))
            num_2 = float(non_digit_strip(num_str_2))
        except ValueError:
            return None

        try:
            return PriceType.comparator(num_1, num_2)
        except ValueError:
            return None

    
