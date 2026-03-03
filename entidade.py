class Entidade:
    def __init__(self, nome: str, poder: int, defesa: int, vida_maxima: int, esquiva: int):
        self.nome = nome
        self.poder = poder
        self.defesa = defesa
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.esquiva = esquiva

    def esta_vivo(self):
        return self.vida_atual > 0

    def receber_dano(self, dano: int):
        self.vida_atual -= dano
        
        if self.vida_atual < 0:
            self.vida_atual = 0

        print(f"{self.nome} recebeu {dano} de dano.")
        print(f"Vida atual: {self.vida_atual}")

    def curar(self, valor: int):
        self.vida_atual += valor

        if self.vida_atual > self.vida_maxima:
            self.vida_atual = self.vida_maxima

        print(f"{self.nome} curou {valor} de vida.")
        print(f"Vida atual: {self.vida_atual}")



heroi = Entidade("ZeCranel", 50, 20, 100, 10)

print("Está vivo?", heroi.esta_vivo())

heroi.receber_dano(30)
heroi.receber_dano(80)

print("Está vivo?", heroi.esta_vivo())

heroi.curar(50)