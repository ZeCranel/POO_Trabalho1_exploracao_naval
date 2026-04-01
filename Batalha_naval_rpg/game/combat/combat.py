
def battle(s, enemy, c):
    while s.hp > 0 and enemy.hp > 0:
        print("\n--- COMBATE ---")
        print(f"Seu HP: {s.hp} | Inimigo HP: {enemy.hp}")

        escolha = input("1-Atacar 2-Defender 3-Fugir: ")

        if escolha == "1":
            damage = max(0, s.atk - enemy.defense)
            enemy.hp -= damage
            print(f"Você causou {damage} de dano!")

        # turno inimigo
        if enemy.hp > 0:
            damage = max(0, enemy.atk - s.defense)
            s.hp -= damage
            print(f"Inimigo causou {damage} de dano!")

    if s.hp <= 0:
        print("Você perdeu!")
    else:
        print("Você venceu!")