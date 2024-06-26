from dandb.data import Type


class Column:

    def __init__(self, column_name: str, data_type: Type = Type.NULL):
        self.column_name: str = column_name
        self.type: Type = data_type