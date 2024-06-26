from typing import Any
from dandb.data import Data
from dandb.column import Column
from dandb.condition import Condition


class CreateDB:

    def __init__(self, dbname: str):
        self.command = "create_db"
        self.dbname = dbname


class SelectDB:

    def __init__(self, dbname: str):
        self.command = "select_db"
        self.dbname = dbname


class CreateTable:

    def __init__(self, table_name: str, schema: list[Column]) -> None:
        self.command = "create_table"
        self.table_name = table_name
        self.schema = schema


class Write:

    def __init__(self, table: str, values: list[Data]) -> None:
        self.command = "write"
        self.table = table
        self.values = values


class Fetch:

    def __init__(self, table: str, conditions: list[Condition], fetchone=False) -> None:
        self.command = "fetch"
        self.table = table
        self.conditions = conditions
        self.fetchone = fetchone


class Update:

    def __init__(
        self, table: str, conditions: list[Condition], delta: list[tuple[str, Any]]
    ):
        self.command = "update"
        self.table = table
        self.conditions = conditions
        self.delta = delta


class Delete:

    def __init__(self, table: str, conditions: list[Condition]):
        self.command = "delete"
        self.table = table
        self.conditions = conditions
