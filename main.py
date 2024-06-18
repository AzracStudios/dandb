from dandb.database import Database
from dandb.row import Column, Row
from dandb.data import Type, Data
from dandb.constraint import Constraint, Operation
from dandb.prettyprint import pretty_print

if __name__ == "__main__":
    db = Database("myfirstdb")

    table = db.get_table("drink")

    if not table:  # create table if not exists
        table = db.create_table("drink")
        print(table)

        schema = [
            Column("sno", Type.INT),
            Column("name", Type.STRING),
            Column("age", Type.INT),
            Column("gender", Type.STRING),
            Column("candrink", Type.INT),
        ]
        table.set_schema(schema)

    row1 = Row(
        [
            Data(Type.INT, 1),
            Data(Type.STRING, "Ram"),
            Data(Type.INT, 16),
            Data(Type.STRING, "Male"),
            Data(Type.INT, 0),
        ]
    )

    row2 = Row(
        [
            Data(Type.INT, 2),
            Data(Type.STRING, "Sam"),
            Data(Type.INT, 22),
            Data(Type.STRING, "Male"),
            Data(Type.INT, 0),
        ]
    )

    row3 = Row(
        [
            Data(Type.INT, 3),
            Data(Type.STRING, "John"),
            Data(Type.INT, 27),
            Data(Type.STRING, "Male"),
            Data(Type.INT, 0),
        ]
    )

    print("\nCREATE")

    # table.create(row1)
    # table.create(row2)
    # table.create(row3)
    # db.commit()

    # print(table)
    # table.delete([Constraint("sno", Operation.EQUAL, 2)])
    # table.update([Constraint("sno", Operation.EQUAL, 3)], [("sno", Data(Type.INT, 2))])

    print("\nFETCH ALL")
    # val = table.fetch_all([Constraint("sno", Operation.NOT_EQUAL, None)])
    # print(val)
    print(table)

    # print("\nFETCH ONE")
    # val = table.fetch_one([Constraint("name", Operation.EQUAL, "Ram")])
    # print(val)

    print("\nUPDATE [can drink]")
    table.update(
        [Constraint("age", Operation.GREATER_THAN_EQUAL, 21)],
        [("candrink", Data(Type.INT, 1))],
    )
    table.update(
        [Constraint("age", Operation.LESS_THAN, 21)], [("candrink", Data(Type.INT, 0))]
    )

    val = table.fetch_all([Constraint("sno", Operation.NOT_EQUAL, None)])
    print(pretty_print(table.schema, val))
    db.commit()

    # print("\nDELETE")
    # table.delete([Constraint("name", Operation.EQUAL, "Ram")])

    # val = table.fetch_all([Constraint("sno", Operation.NOT_EQUAL, None)])
    # print(val)
