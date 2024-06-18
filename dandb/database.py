import os, pathlib, pickle
from dandb.table import Table


class Database:

    def __init__(self, name: str):
        self.name: str = name
        self.tables: list[Table] = []
        self.index_hash: dict[str, int] = {}
        self.path_to_load: str = ""

        self.configure_path()
        self.load()

    def configure_path(self):
        self.path_to_load = os.path.join(
            pathlib.Path(__file__).parent.resolve().parent.resolve(),
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

        with open(self.path_to_load, "rb") as f:
            self.tables = pickle.load(f)
            for i, table in enumerate(self.tables):
                self.index_hash[table.name] = i

    def get_table(self, name):
        if name not in self.index_hash.keys():
            return None  # TODO: RAISE EXCEPTION

        return self.tables[self.index_hash[name]]

    def create_table(self, name: str):
        if name in self.index_hash.keys():
            return None  # TODO: RAISE EXCEPTION

        table = Table(name)
        self.tables.append(table)
        self.index_hash[name] = len(self.tables) - 1

        return self.get_table(name)
