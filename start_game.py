import character
import enemies


def start():
    player = character.create_character()
    enemy_list = enemies.generate_random_enemies()

    # Continuar o jogo
