import random


class Character:
    def __init__(self, name, char_class, health, mana, strength, intelligence, agility):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.mana = mana
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility


def create_character():
    name = input("Enter your character name: ")
    char_class = input("Enter your character class (Mage, Tank, Warrior, Archer): ")
    if char_class == "Mage":
        health = random.randint(50, 100)
        mana = random.randint(100, 150)
        strength = random.randint(10, 30)
        intelligence = random.randint(60, 100)
        agility = random.randint(20, 40)
    elif char_class == "Tank":
        health = random.randint(100, 150)
        mana = random.randint(50, 100)
        strength = random.randint(60, 100)
        intelligence = random.randint(10, 30)
        agility = random.randint(20, 40)
    elif char_class == "Warrior":
        health = random.randint(80, 130)
        mana = random.randint(30, 80)
        strength = random.randint(50, 90)
        intelligence = random.randint(20, 50)
        agility = random.randint(30, 60)
    elif char_class == "Archer":
        health = random.randint(60, 110)
        mana = random.randint(40, 90)
        strength = random.randint(30, 70)
        intelligence = random.randint(30, 70)
        agility = random.randint(50, 90)
    else:
        print("Invalid character class.")
        return None
    return Character(name, char_class, health, mana, strength, intelligence, agility)
