import os, pathlib, pickle
from dandb.table import Table
import dansql.command as command
from dandb.column import Column


class Database:

    def __init__(self):
        self.name: str | None = None
        self.tables: dict[str, Table] = {}
        self.path_to_load: str = ""
        self.db_initialized: bool = False

    def configure_path(self):
        self.path_to_load = os.path.join(
            pathlib.Path(__file__).parent.parent.resolve(),
            "databases",
            f"{self.name}.dandb",
        )

        # create file if not exists
        if not os.path.exists(self.path_to_load):
            with open(self.path_to_load, "w") as f:
                f.write("")

    def commit(self):
        # write all tables to file
        with open(self.path_to_load, "wb") as f:
            pickle.dump(self.tables, f)

    def load(self):
        # quit if file is empty
        if os.path.getsize(self.path_to_load) == 0:
            return

        # load tables and generate hash
        with open(self.path_to_load, "rb") as f:
            self.tables = pickle.load(f)

    def execute(self, command):
        return getattr(self, command.command)(command)

    def create_db(self, command: command.CreateDB):
        if self.db_initialized:
            self.commit()
             
        self.name = command.dbname

        self.configure_path()
        self.load()

        self.db_initialized = True

    def select_db(self, command: command.SelectDB):
        if self.tables:
            self.commit()

        self.name = command.dbname

        self.configure_path()
        self.load()

    # def create_table(self, command: command.CreateTable):
    #     if command.table_name in self.tables.keys():
    #         return None


    def get_table(self, name):
        if name not in self.tables.keys():
            return None  # TODO: RAISE EXCEPTION

        return self.tables[name]

    def create_table(self, name: str, schema: list[Column]):
        if name in self.tables.keys():
            return None  # TODO: RAISE EXCEPTION

        table = Table(name, schema=schema)
        self.tables[name] = table

        return self.get_table(name)
