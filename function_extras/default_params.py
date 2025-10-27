
# function params with default values
def calculate_weight(mass: float, g: float = 9.81) -> float:
    """ computes weight given gravitational constant """
    return mass * g


# calling the function with default values,
calculate_weight(10)
calculate_weight(10, 3.75)

# calling the function with named arguments
calculate_weight(g=3.75, mass=10)

# a simple lambda function
add_two = lambda x : x + 2
result = add_two(5) # result = 7

# a multi-parameter lambda function
add_two_numbers = lambda x, y : x + y
result = add_two_numbers(3, 4) # returns 7

# the equivalent "normal" function:
def add_two_numbers(x, y):
    return x + y

# a lambda function in action
score = {'alice': 5, 'bob': 3, 'charley': 4}

winner = max(score, key=lambda name: score[name])
print(winner)


def weighted_avg(numbers: list, weights: list = None) -> float:
    """
    return average of numbers
    OR, if weights are supplied, return weighted average of numbers
    """
    if weights is None:
        return sum(numbers) / len(numbers)
    else: # if something was passed in for weights
        weighted_sum = 0
        for i in range(len(numbers)):
            weighted_sum += numbers[i] * weights[i]
        return weighted_sum / sum(weights)

print(weighted_avg([1, 2, 3]))
print(weighted_avg([1, 2, 3], [2, 1, 1]))
