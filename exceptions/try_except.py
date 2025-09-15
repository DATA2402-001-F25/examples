try:
    number = float(input('enter a number: '))# 0 entered 
    inverse = 1 / number
    print(inverse)
except ZeroDivisionError:
    print('Error')

# note we can still get an (unhandled) ValueError that crashes the program
# if user enters a non-number on line 2

