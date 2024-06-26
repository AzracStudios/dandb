from typing import Any
from dandb.data import Data
from dandb.column import Column

class Row:

    def __init__(
        self,
        values: list[Data],
        schema: dict[str, Column]
    ):
        self.schema = schema
        self.values = self.generate_values(values)

    def check_types(self):
        if len(self.values) != len(self.schema):
            return False  # TODO: RAISE EXCEPTION

        for column, value in self.values.items():
            if value.type != self.schema[column].type:
                return False  # TODO: RAISE EXCEPTION

        return True

    def generate_values(self, values: list[Data]) -> dict[str, Data]:
        vals_dict = {}

        for i, column_name in enumerate(self.schema):
            vals_dict[column_name] = values[i]

        return vals_dict

    def get_column(self, column_name):
        if not column_name in self.values.keys():
            return False  # TODO: RAISE EXCEPTION

        return self.values[column_name]

    def update(self, delta: list[tuple[str, Any]]):
        for column_name, value in delta:
            if not self.get_column(column_name):
                return False  # TODO: RAISE EXCEPTION

            self.values[column_name] = value

    def __repr__(self):
        return "  ".join([str(data.value) for data in self.values])
