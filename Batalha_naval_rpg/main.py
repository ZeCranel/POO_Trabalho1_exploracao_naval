
from game.captain.factory import create_captain
from game.ships.factory import create_ship
from game.combat.combat import battle
import random

print("""nesse mundo você tem a opção de se aventurar como 3 capitães Piratas
Pirata Veterano: Sofreu um motim da sua tripulação e agora está atrás de vingança apenas com um navio pequeno

Pirata Junior: Cansou de esfregar convés e está saindo ao mundo com o sonho de ser o maior capitão da atualidade

Pirata Aprendiz: Saiu da sua terra natal sem experiencia apenas com um sonho e seus amigos""")


def escolher_capitao():
    while True:
        print("\n1-Pirata Veterano\n2-Pirata Junior\n3-Pirata Aprendiz\n4-Info")
        e=input(">> ")
        if e in ["1","2","3"]: return create_captain(e)
        if e=="4":
            print("Veterano: furtivo, só navio pequeno")
            print("Junior: equilibrado, Todos os navios")
            print("Aprendiz: Sem experiencia, so navio medio e pequeno")

def escolher_navio(c):
    while True:
        print("\n1-Navio Pequeno\n2-Navio Médio\n3-Navio Grande\n4-Info")
        e=input(">> ")
        if e=="4":
            print("Pequeno ATK3 DEF2 HP10 Furtividade alta")
            print("Médio ATK5 DEF4 HP15 Furtividade média")
            print("Grande ATK7 DEF6 HP20 Furtividade baixa")
            continue
        s=create_ship(e)
        if not s: continue
        if not c.can_use(s.name):
            print("Capitão não pode usar")
            continue
        return s

def explorar(s,c):
    evento=random.choice(["pirata","fragata","galeao","ilha","ilha_perigosa"])
    print("Evento:",evento)

    if evento in ["pirata","fragata","galeao"]:
        detect = random.random() < (s.stealth + c.detect)
        print("Navio visto")
        if detect:
            print("Você foi detectado")
            enemy=create_ship(str(random.randint(1,3)))
            battle(s,enemy,c)
        else:
            print("Não foi detectado")
            print("1-Atacar 2-Fugir")
            e=input(">> ")
            if e=="1":
                enemy=create_ship(str(random.randint(1,3)))
                battle(s,enemy,c)

    elif evento=="ilha":
        print("Ilha segura encontrada. Você coletou recursos")

    elif evento=="ilha_perigosa":
        print("Ilha desconhecida")
        inimigos=random.choice([True,False])
        if not inimigos:
            print("Sem inimigos, loot obtido")
        else:
            print("Há inimigos")
            detect = random.random() < c.detect
            if detect:
                print("Você foi detectado ao sair")
                enemy=create_ship("2")
                battle(s,enemy,c)
            else:
                print("Você escapou sem ser visto")

def status(s,c):
    print(f"Navio: {s.name}")
    print(f"HP: {s.hp}/{s.max_hp}")
    print(f"ATK: {s.atk} DEF: {s.defense}")
    print(f"Furtividade: {s.stealth}")
    print(f"Capitão: {c.name} Nivel: {c.level}")

def jogo():
    c=escolher_capitao()
    s=escolher_navio(c)
    while True:
        print("\n1-Explorar\n2-Status\n3-Reparar\n4-Upgrade\n5-Sair")
        e=input(">> ")
        if e=="1": explorar(s,c)
        elif e=="2": status(s,c)
        elif e=="3": s.repair()
        elif e=="4": s.upgrade()
        elif e=="5": break

if __name__=="__main__":
    jogo()
