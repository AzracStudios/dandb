from enum import Enum
from typing import Any

class Type(Enum):
    NULL = 1
    INT = 2
    FLOAT = 3
    STRING = 4


class Data:

    def __init__(self, type: Type, value: Any):
        self.type: Type = type
        self.value = value
        self.column_name = None

    def __repr__(self):
        return str(self.value)
