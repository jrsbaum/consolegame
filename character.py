import random


class Character:
    def __init__(self, name: str, char_class: str, health: int, mana: int, strength: int, intelligence: int, agility: int, defense: float):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.mana = mana
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility
        self.defense = defense


def create_character():
    name = input("Entre com o nome do seu personagem: ")
    char_class = input("Entre com a classe do seu personagem: (Mago, Tank, Guerreiro, Arqueiro): ")
    if char_class == "Mago":
        health: int = 100
        mana = random.randint(100, 150)
        strength = random.randint(10, 30)
        intelligence = random.randint(60, 100)
        agility = random.randint(20, 40)
        defense: int = 20
    elif char_class == "Tanque":
        health: int = 123
        mana = random.randint(50, 100)
        strength = random.randint(60, 100)
        intelligence = random.randint(10, 30)
        agility = random.randint(20, 40)
        defense = 42
    elif char_class == "Guerreiro":
        health: int = 109
        mana = random.randint(30, 80)
        strength = random.randint(50, 90)
        intelligence = random.randint(20, 50)
        agility = random.randint(30, 60)
        defense: int = 34
    elif char_class == "Arqueiro":
        health: int = 98
        mana = random.randint(40, 90)
        strength = random.randint(30, 70)
        intelligence = random.randint(30, 70)
        agility = random.randint(50, 90)
        defense: int = 24
    else:
        print("Classe invalida.")
        return None
    return Character(name, char_class, health, mana, strength, intelligence, agility, defense)

