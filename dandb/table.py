from __future__ import annotations
from dandb.prettyprint import pretty_print
from dandb.data import Data
from dandb.row import Row
from dandb.column import Column
from dandb.condition import Condition


class Table:

    def __init__(self, name: str, rows: list[Row] = [], schema: list[Column] = []):
        self.name: str = name

        self.schema: dict[str, Column] = {}
        self.set_schema(schema)

        self.table: list[Row] = rows

    def set_schema(self, schema: list[Column]):
        for column in schema:
            self.schema[column.column_name] = column

    def create(self, values: list[Data]):
        row = Row(values, self.schema)

        if not row.check_types():
            return

        self.table.append(row)

    def fetch_one(self, conditions: list[Condition]) -> Table | None:
        for row in self.table:
            constraints_passed = 0

            for constraint in conditions:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(conditions):
                return Table("_", rows=[row], schema=self.schema.values())

        return None

    def fetch_all(self, conditions: list[Condition]) -> Table:
        rows = []

        for row in self.table:
            constraints_passed = 0

            for constraint in conditions:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(conditions):
                rows.append(row)

        return Table("_", rows=rows, schema=self.schema.values())

    def update(self, conditions: list[Condition], delta) -> Row:
        updated_rows = []

        for row in self.table:
            constraints_passed = 0

            for constraint in conditions:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(conditions):
                row.update(delta)
                updated_rows.append(row)

        return Table("_", rows=updated_rows, schema=self.schema.values())

    def delete(self, conditions):
        rows_to_delete = []
        for i, row in enumerate(self.table):
            constraints_passed = 0

            for constraint in conditions:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(conditions):
                rows_to_delete.append((i, row))

        for i, row in rows_to_delete:
            self.table.pop(i)
            del row

    def __repr__(self):
        return pretty_print(self.schema, self.table)
