import psutil
import time
import json
from datetime import date

global Dados
Info = "Informações.json"  

horas = 0
minutos = 0
segundos = 0

dataNumero = date.today().weekday()
nomeSemana = ["Seg","Ter","Qua","Qui","Sex","Sab","Dom"]
data = nomeSemana[dataNumero]


while ( "Code.exe" in (i.name() for i in psutil.process_iter()) ):
                
    with open(Info, 'r') as arquivo:
        arq = json.load(arquivo)
        arq[f"{data}"] = (f"{horas}h {minutos}m {segundos}s")
                    
    with open(Info, "w") as f:
        json.dump(arq, f)
                    

    time.sleep(1)
    segundos += 1
    print(f"\rAberto por {horas}h {minutos}m {segundos}s", end="")

    if segundos == 60: # minutos
        segundos = 0
        minutos += 1
                    
                
                
    if minutos == 60: # hora
        minutos = 0
        horas += 1
        
 
    



