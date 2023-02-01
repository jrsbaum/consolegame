import random


class Character:
    def __init__(self, name: str, char_class: str, health: int, mana: int, strength: int, intelligence: int, agility: int):
        self.name = name
        self.char_class = char_class
        self.health = health
        self.mana = mana
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility


def create_character():
    name = input("Entre com o nome do seu personagem: ")
    char_class = input("Entre com a classe do seu personagem: (Mago, Tank, Guerreiro, Arqueiro): ")
    if char_class == "Mago":
        health = random.randint(50, 100)
        mana = random.randint(100, 150)
        strength = random.randint(10, 30)
        intelligence = random.randint(60, 100)
        agility = random.randint(20, 40)
    elif char_class == "Tanque":
        health = random.randint(100, 150)
        mana = random.randint(50, 100)
        strength = random.randint(60, 100)
        intelligence = random.randint(10, 30)
        agility = random.randint(20, 40)
    elif char_class == "Guerreiro":
        health = random.randint(80, 130)
        mana = random.randint(30, 80)
        strength = random.randint(50, 90)
        intelligence = random.randint(20, 50)
        agility = random.randint(30, 60)
    elif char_class == "Arqueiro":
        health = random.randint(60, 110)
        mana = random.randint(40, 90)
        strength = random.randint(30, 70)
        intelligence = random.randint(30, 70)
        agility = random.randint(50, 90)
    else:
        print("Classe invalida.")
        return None
    return Character(name, char_class, health, mana, strength, intelligence, agility)

