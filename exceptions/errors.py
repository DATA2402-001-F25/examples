
# example of a syntax error
#3d_map = 5


# example of a runtime error
my_string = 'hello world'
# my_string[11]

# example (possible) runtime error
from math import sqrt, pi

def radius(area: float) -> float:
    'calculate a circle radius given its area'
    return sqrt(area / pi)    # runtime error if area is negative

area = float(input('enter circle area: '))  # runtime error if user enters a non-number
print(f'radius = {radius(area)}')


