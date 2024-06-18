from enum import Enum
from typing import Any

class Operation(Enum):
    EQUAL = 0
    LESS_THAN = 1
    GREATER_THAN = 2
    LESS_THAN_EQUAL = 3
    GREATER_THAN_EQUAL = 4
    NOT_EQUAL = 5


class Constraint:

    def __init__(self, col_to_check: str, operation: Operation, expected_value: Any):
        self.col_to_check = col_to_check
        self.operation = operation
        self.expected_value = expected_value

    def evaluate(self, row):
        match self.operation:
            case Operation.EQUAL:
                if row.get_column(self.col_to_check).value == self.expected_value:
                    return True

            case Operation.LESS_THAN:
                if row.get_column(self.col_to_check).value < self.expected_value:
                    return True

            case Operation.GREATER_THAN:
                if row.get_column(self.col_to_check).value > self.expected_value:
                    return True

            case Operation.LESS_THAN_EQUAL:
                if row.get_column(self.col_to_check).value <= self.expected_value:
                    return True

            case Operation.GREATER_THAN_EQUAL:
                if row.get_column(self.col_to_check).value >= self.expected_value:
                    return True

            case Operation.NOT_EQUAL:
                if row.get_column(self.col_to_check).value != self.expected_value:
                    return True

        return False