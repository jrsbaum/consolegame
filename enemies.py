import random


class Enemy:
    def __init__(self, name, health, mana, strength, intelligence, agility):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.intelligence = intelligence
        self.agility = agility


def generate_random_enemies():
    enemies = []
    enemy_types = ['Orc', 'Goblin', 'Troll', 'Dragon', 'Skeleton']
    for i in range(5):
        enemy = random.choice(enemy_types)
        health = random.randint(50, 100)
        mana = random.randint(50, 100)
        strength = random.randint(50, 100)
        intelligence = random.randint(50, 100)
        agility = random.randint(50, 100)
        enemies.append(Enemy(enemy, health, mana, strength, intelligence, agility))
    return enemies


def generate_random_bosses():
    bosses = []
    boss_types = ['Dark Knight', 'Witch Queen', 'Giant Kraken', 'Gran Lord', 'The Necromancer']
    for i in range(3):
        boss = random.choice(boss_types)
        health = random.randint(100, 200)
        mana = random.randint(100, 200)
        strength = random.randint(100, 200)
        intelligence = random.randint(100, 200)
        agility = random.randint(100, 200)
        bosses.append(Enemy(boss, health, mana, strength, intelligence, agility))
    return bosses