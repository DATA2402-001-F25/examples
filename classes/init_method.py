class Character:

    def __init__(self, character_name: str, character_hp: int) -> None:
        self.name = character_name
        self.hit_points = character_hp


my_character = Character('Eric', 5)
print(f'{my_character.name} has {my_character.hit_points} hp')

my_other_character = Character('Magid', 10_000)
print(my_other_character.name, my_other_character.hit_points)

# modify first character's hp
my_character.hit_points -= 3
print(f'{my_character.name} hp is now {my_character.hit_points}')

