
def process_an_integer(x: int) -> None:
    """
    raise an exception if something other than int is passed in
    """
    # do the check here
    if type(x) != int:
        raise Exception('must be int')

    # this doesn't work because x is not a datatype
    # x == int  always returns False

    print(x)


process_an_integer(5)