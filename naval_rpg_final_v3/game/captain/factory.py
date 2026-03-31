
from .captain import Captain
def create_captain(c):
    if c=="1": return Captain("Veterano",2,2,0.0,["Pequeno"])
    if c=="2": return Captain("Aprendiz",1,1,0.5,["Pequeno","Médio","Grande"])
    if c=="3": return Captain("Iniciante",0,0,0.5,["Pequeno","Médio"])
