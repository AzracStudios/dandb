import math


def generate_space(cell_width: int, content_width: int) -> tuple[str, str]:
    factor = (cell_width - content_width) / 2

    if int(factor) == factor:
        return (" " * int(factor), " " * int(factor))

    return (" " * int(factor - 0.5), " " * int(factor + 0.5))


def pretty_print(schema, rows):
    column_width = {}

    if not len(rows):
        return ""

    # compute width for all columns
    for row in rows:
        for column, value in row.values.items():
            existing_buffer = column_width.get(column, None)

            if existing_buffer == None or existing_buffer < len(f"{value.value}"):
                column_width[column] = len(f"{value.value}")

    # the width values must be revisited, since it is a possibility
    # that the width of the largest item is less than the column name itself
    border = "+"
    for column, count in column_width.items():
        length_to_set = count

        if len(column) > length_to_set:
            length_to_set = len(column)

        column_width[column] = length_to_set + 2

        # generate classic mysql border
        border += f'{"-" * column_width[column]}+'

    # create table header
    header = "|"

    for column, value in schema.items():
        lspace, rspace = generate_space(column_width[column], len(column))
        header += f"{lspace}{column}{rspace}|"

    vals = ""
    for row in rows:
        vals += "|"
        for column, value in row.values.items():
            lspace, rspace = generate_space(column_width[column], len(f"{value.value}"))
            vals += f"{lspace}{value}{rspace}|"

        vals += "\n"

    return f"{border}\n{header}\n{border}\n{vals}{border}"
