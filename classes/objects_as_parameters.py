"""
Add a third data attribute to Character, called “damage”
Create two characters, and write a function called “attack” 
that accepts 2 Character objects as parameters, and subtracts 
the first character’s damage from the second character’s hit points.
"""

class Character:

    def __init__(self, character_name: str, character_hp: int, damage:int) -> None:
        """
        docstring
        """
        self.name = character_name
        self.hit_points = character_hp
        self.damage = damage
    

characterA = Character('eric', 5, 2)
characterB = Character('Han', 100, 10)

def attack(attacker: Character, victim: Character) -> None:
    victim.hit_points -= attacker.damage
