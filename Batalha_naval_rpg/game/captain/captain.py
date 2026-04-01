
class Captain:
    def __init__(self,name,atk,defb,detect,allowed):
        self.name=name
        self.atk_bonus=atk
        self.def_bonus=defb
        self.detect=detect
        self.allowed=allowed
        self.level=1
    def can_use(self,s): return s in self.allowed
