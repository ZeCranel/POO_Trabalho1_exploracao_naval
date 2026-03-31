
from game.data.dice import d20, chance

def battle(p,e,c):
    print("Combate iniciado")
    while p.is_alive() and e.is_alive():
        print("1-Atacar 2-Fugir")
        ac=input(">> ")
        if ac=="2":
            if chance(0.5):
                print("Você fugiu")
                return
            else:
                print("Falhou ao fugir")

        if d20()+p.atk+c.atk_bonus > d20()+e.defense:
            e.hp-=2; print("Você acertou")
        else:
            print("Você errou")

        if not e.is_alive():
            print("Vitória")
            return

        if d20()+e.atk > d20()+p.defense+c.def_bonus:
            p.hp-=2; print("Você tomou dano")
        else:
            print("Inimigo errou")
