# round brackets makes it a tuple
my_tuple = (1, 2, 3)  # brackets can be omitted too: my_tuple = 1, 2, 3

# tuples are immutable
# my_tuple[2] = 4 # this is a runtime error

# but you can still access their contents by index
print(my_tuple[0])

# unpacking tuples 
tup = 1, 2, 3
a, b, c = tup

l = [1, 2, 3]
a, b, c = l
print(a, b, c)



# searching for something in a list
def search(the_list: list, the_target: str) -> int:
    """
    search for the_target in the_list, return its index
    return -1 if not found
    """
    for index in range(len(the_list)):
        if the_list[index] == the_target:
            return index
    return -1

