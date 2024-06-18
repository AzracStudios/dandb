import math


def pretty_print(schema, rows):
    print_buffer = {}

    if not len(rows):
        return ""

    for column in schema:
        print_buffer[column.column_name] = []

    for row in rows:
        for column, value in row.as_pairs(schema):
            print_buffer[column].append(f"{value}")

    # HEADER ROW
    top_btm_border = "+"

    for column in schema:
        print_buffer[column.column_name] = (
            max(len(column.column_name), len(max(print_buffer[column.column_name]))) + 2
        )

        top_btm_border += "-" * print_buffer[column.column_name]
        top_btm_border += "+"

    header = "|"

    for column in schema:
        space = " " * math.ceil(
            (print_buffer[column.column_name] - len(column.column_name)) / 2
        )

        header += space + column.column_name + space + "|"

    vals = ""
    for row in rows:
        vals += "|"
        for column, value in row.as_pairs(schema):
            numspaces = (print_buffer[column] - len(str(value))) / 2
            if int(numspaces) == numspaces:
                vals += (
                    (" " * int(numspaces)) + str(value) + (" " * int(numspaces)) + "|"
                )
            else:
                space = " " * int(numspaces - 0.5)
                vals += (
                    (" " * int(numspaces))
                    + str(value)
                    + (" " * int(numspaces + 0.5))
                    + "|"
                )

        vals += "\n"

    return (
        top_btm_border
        + "\n"
        + header
        + "\n"
        + top_btm_border
        + "\n"
        + vals
        + top_btm_border
    )
