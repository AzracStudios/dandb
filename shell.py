from dandb.database import Database, Column
from dandb.data import Data, Type
from dandb.condition import Condition, Operation

written_cnt = -1
db = Database()


data = [
    (
        Data(Type.INT, 1),
        Data(Type.STRING, "Bob"),
        Data(Type.STRING, "abc@xyz.com"),
        Data(Type.STRING, "123"),
    ),
    (
        Data(Type.INT, 2),
        Data(Type.STRING, "Sam"),
        Data(Type.STRING, "xyz@abc.com"),
        Data(Type.STRING, "456"),
    ),
    (
        Data(Type.INT, 3),
        Data(Type.STRING, "Rob"),
        Data(Type.STRING, "123@xyz.com"),
        Data(Type.STRING, "789"),
    ),
    (
        Data(Type.INT, 4),
        Data(Type.STRING, "Jim"),
        Data(Type.STRING, "xyz@123.com"),
        Data(Type.STRING, "abc"),
    ),
]


def eval(src):
    tokens = src.split(" ")

    if tokens[0] == "select":
        db.name = tokens[2][:-2]
        db.configure_path()
        db.load()

    if tokens[0] == "create":
        if tokens[1] == "database":
            db.name = tokens[2][:-2]
            db.configure_path()
            db.load()

        if tokens[1] == "table":
            db.create_table(
                tokens[2],
                [
                    Column("id", Type.INT),
                    Column("name", Type.STRING),
                    Column("email", Type.STRING),
                    Column("password", Type.STRING),
                ],
            )

    if tokens[0] == "write":
        global written_cnt
        written_cnt += 1
        to_write = data[written_cnt]
        db.get_table("users").create(to_write)

    if tokens[0] == "fetchall":
        if tokens[3][-2] == ";":
            print(db.get_table("users").fetch_all([]))

        else:
            if "Bob" in src:
                print(
                    db.get_table("users").fetch_all(
                        [Condition("name", Operation.EQUAL, "Bob")]
                    )
                )

            elif "id" in src:
                print(
                    db.get_table("users").fetch_all(
                        [Condition("id", Operation.GREATER_THAN, 2)]
                    )
                )

    if tokens[0] == "fetchone":
        if "update" not in src:
            if "Sam" in src:
                print(
                    db.get_table("users").fetch_one(
                        [Condition("name", Operation.EQUAL, "Sam")]
                    )
                )

            elif "id" in src:
                print(
                    db.get_table("users").fetch_one(
                        [Condition("id", Operation.GREATER_THAN, 2)]
                    )
                )

        else:
            db.get_table("users").update(
                [Condition("name", Operation.EQUAL, "Bob")],
                [("name", Data(Type.STRING, "Bob cat"))],
            )

    if "delete" in src:
        db.get_table("users").delete([Condition("name", Operation.EQUAL, "Jim")])

    if "commit" in src:
        db.commit()


def shell():
    print("DanDB Shell v1.0")
    src = ""

    building_src = False

    while True:
        line = input(">>> " if not building_src else "... ")
        if line == "":
            continue
        building_src = True if not building_src else building_src

        if line.lower() == "exit":
            quit()

        src += line + "\n"
        if line[-1] == ";":
            building_src = False
            eval(src)

            src = ""
