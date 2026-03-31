
from .ship import Ship
def create_ship(c):
    if c=="1": return Ship("Pequeno",3,2,10,0.2)
    if c=="2": return Ship("Médio",5,4,15,0.5)
    if c=="3": return Ship("Grande",7,6,20,0.8)
