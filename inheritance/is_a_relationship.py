class Vertebrate:

    def __init__(self, n_vertebrae: int):
        self.number_of_vertebrae = n_vertebrae


class Frog(Vertebrate):

    def __init__(self, poisonous: bool):
        self.poisonous = poisonous
        super().__init__(10)  # if not all frogs had 10, we could make this a parameter of Frog's __init__


kermit = Frog(False)
print(type(kermit))
print(type('hello'))

print(isinstance(kermit, Frog))
print(isinstance(kermit, str))

print(isinstance(kermit, Vertebrate)) # isinstance respects inheritance
print(isinstance(kermit, Frog)) # isinstance respects inheritance
