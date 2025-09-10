# Write a function that accepts a table of data, formatted as a 2D list, with inner lists representing the rows of the table.
# The table is expected to contain exactly 3 columns. That is, each row should have 3 elements.
# Make the function raise an exception if the table is the wrong size.

table = [
    [1, 2, 3],
    [2, 3, 4],
    [3, 2, 1],
    [3, 3, 2, 1], # this row is wrong
    [2, 2, 2],
    [1, 2, 3],
    # could be more rows...
]

def table_validator(table: list) -> None:
    """
    check the table to ensure it has 3 columns. raise an exception if not.
    """
    # one way to write the loop
    for row_idx in range(0, len(table)):
        if len(table[row_idx]) != 3:
            raise Exception(f"row #{row_idx} has wrong # of columns")

    # other way
    # for row in table:
    #     if len(row) != 3:
    #         raise Exception("detected a row with wrong number of columns")

table_validator(table)