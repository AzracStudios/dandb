from typing import Any
from dandb.data import Type, Data


class Column:

    def __init__(self, column_name: str, data_type: Type = Type.NULL):
        self.column_name: str = column_name
        self.type: Type = data_type


class Row:

    def __init__(
        self,
        values: list[Data],
        index_hash: dict[str, int] = {},
        primary: Data | None = None,
    ):
        self.values = values
        self.index_hash = index_hash
        self.primary = primary

    def check_types(self, schema):
        if len(self.values) != len(schema):
            return False  # TODO: RAISE EXCEPTION

        for i, value in enumerate(self.values):
            if value.type != schema[i].type:
                return False  # TODO: RAISE EXCEPTION

        return True

    def populate_col_name(self, schema):
        for i, value in enumerate(self.values):
            value.column_name = schema[i].column_name

        return True

    def get_column(self, col_name):
        if not col_name in self.index_hash.keys():
            return False  # TODO: RAISE EXCEPTION

        return self.values[self.index_hash[col_name]]

    def update(self, delta: list[tuple[str, Any]]):
        for colname, value in delta:
            if not self.get_column(colname):
                return False  # TODO: RAISE EXCEPTION

            self.values[self.index_hash[colname]] = value

    def as_pairs(self, schema):
        to_ret = []

        for i, data in enumerate(self.values):
            to_ret.append((schema[i].column_name, data))

        return to_ret

    def __repr__(self):
        return "  ".join([str(data.value) for data in self.values])
