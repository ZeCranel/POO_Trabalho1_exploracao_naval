
class Ship:
    def __init__(self,name,atk,defense,hp,stealth):
        self.name=name
        self.atk=atk
        self.defense=defense
        self.max_hp=hp
        self.hp=hp
        self.stealth=stealth
    def is_alive(self): return self.hp>0
    def repair(self): self.hp=self.max_hp
    def upgrade(self):
        self.atk+=1; self.defense+=1; self.max_hp+=2; self.hp=self.max_hp
