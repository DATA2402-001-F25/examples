
# create a list by enclosing several values in square brackets
acceptable_flavours = ['vanilla', 'chocolate', 'Neapolitan']
unacceptable_flavours = ['mint-chocolate']

an_empty_list = []

a_list_of_numbers = [1, 2, 3, 4]
mixed_types = [1, "hi", 4.0]

# cast range to list
print(list(range(10)))
print(list('hello world'))


# measure the length of a list (or other collection or sequence) with len
len(acceptable_flavours)
len('hello')

# list methods
acceptable_flavours.append('cookies n cream')
print(acceptable_flavours)

# using "in"
if 'mint chocolate' in acceptable_flavours:
    print('youre dismissed')

# iterating over lists with for
letters =  ['a',  'b',  'c',  'd',  'e']
for letter in letters:
    print(letter)

# iterating through the list when the index of the things matters
for index in range(len(letters)):
    print(f'{letters[index]} at index {index}')

# slicing
days = ['Su', 'M', 'Tu', 'W', 'Tr', 'F', 'Sa']
days[1:3]  # returns ['M', 'Tu']
days[1:] # leave the end off - defaults to the end
days[:4] # leave out the start - defaults to 0
print(days[1:5:2]) # specify a "step" (in this case, every other item)

