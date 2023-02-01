import random
import character
import enemies


def start():
    print("BEM-VINDO!")
    print("Você é um aventureiro corajoso que está em uma missão para derrotar o chefe do mal e salvar o reino.")
    print("Você encontrará muitos inimigos ao longo do caminho e, a cada turno, enfrentará um inimigo aleatório.")
    print("Você está pronto para o desafio? Vamos começar!")

    player = character.create_character()
    enemy_list = enemies.generate_random_enemies()

    while len(enemy_list) > 0:
        # Escolher um inimigo aleatório da lista
        enemy = random.choice(enemy_list)
        enemy_list.remove(enemy)

        # Lógica do combate
        while player.health > 0 and enemy.health > 0:
            # Escolher ação do jogador
            print(f"Sua vida: {player.health}")
            print(f"Vida inimiga: {enemy.health}")
            print("O que você quer fazer?")
            print("1. Atacar")
            print("2. Usar poção")
            action = int(input("Entre com sua escolha: "))

            if action == 1:
                # Calcular dano causado pelo jogador
                damage = enemy.defense - player.strength
                if damage < 0:
                    damage = 0
                enemy.health -= damage
                print(f"Você atacou o inimigo e causou {damage} de dano.")

            elif action == 2:
                # Verificar se o jogador tem poções
                if player.potions > 0:
                    player.health += 50
                    player.potions -= 1
                    print("Você usou uma poção e curou 50 de vida.")
                else:
                    print("Você não tem mais poções.")
                    continue

            # Verificar se o inimigo ainda está vivo
            if enemy.health <= 0:
                print("Você derrotou o inimigo.")
                break

            # Calcular dano causado pelo inimigo
            damage = player.defense - enemy.strength
            if damage < 0:
                damage = 0
            player.health -= damage
            print(f"O inimigo atacou você e causou {damage} de dano.")

        # Verificar se o jogador ainda está vivo
        if player.health <= 0:
            print("Você foi derrotado. Game over.")
            break

    # Verificar se o jogador venceu todos os inimigos
    if len(enemy_list) == 0:
        print("Parabéns! Você derrotou todos os inimigos e salvou o Reino!")
