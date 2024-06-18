from dandb.prettyprint import pretty_print
from dandb.row import Column, Row
from dandb.constraint import Constraint

class Table:

    def __init__(self, name: str):
        self.name: str = name
        self.schema: list[Column] = []
        self.index_hash = {}
        self.table: list[Row] = []

    def set_schema(self, schema):
        self.schema = schema
        for i, column in enumerate(self.schema):
            self.index_hash[column.column_name] = i

    def create(self, row: Row):
        if not row.check_types(self.schema):
            return
        row.populate_col_name(self.schema)
        row.index_hash = self.index_hash
        self.table.append(row)

    def fetch_one(self, constraints: list[Constraint]) -> Row | None:
        for row in self.table:
            constraints_passed = 0

            for constraint in constraints:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(constraints):
                return row
        return None

    def fetch_all(self, constraints: list[Constraint]) -> list[Row]:
        rows = []

        for row in self.table:
            constraints_passed = 0

            for constraint in constraints:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(constraints):
                rows.append(row)

        return rows

    def update(self, constraints, delta) -> Row:
        updated_rows = []

        for row in self.table:
            constraints_passed = 0

            for constraint in constraints:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(constraints):
                row.update(delta)
                updated_rows.append(row)

        return updated_rows

    def delete(self, constraints):
        rows_to_delete = []
        for i, row in enumerate(self.table):
            constraints_passed = 0

            for constraint in constraints:
                if not constraint.evaluate(row):
                    continue
                constraints_passed += 1

            if constraints_passed == len(constraints):
                rows_to_delete.append((i, row))

        for i, row in rows_to_delete:
            self.table.pop(i)
            del row

    def __repr__(self):
        return pretty_print(self.schema, self.table)