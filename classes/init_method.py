class Character:

    def __init__(self, character_name: str, character_hp: int) -> None:
        self.name = character_name
        self.hit_points = character_hp

    def save(self, filename):
        f = open(filename, 'w')
        f.write(self.name + ',' + str(self.hit_points))
        f.close()

class Mage(Character):

    def __init__(self, character_name: str, character_hp: int, spells: list):
        super().__init__(character_name, character_hp)
        self.spells = spells

m = Mage('gandalf', 10, ['frost', 'something else'])
m.save()


my_character = Character('Eric', 5)
print(f'{my_character.name} has {my_character.hit_points} hp')

my_other_character = Character('Magid', 10_000)
print(my_other_character.name, my_other_character.hit_points)

# modify first character's hp
my_character.hit_points -= 3
print(f'{my_character.name} hp is now {my_character.hit_points}')

