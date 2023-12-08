import psutil
import time
import json
from datetime import date

global Aberto, Dados
Aberto = False
Dados = "Data.json"  

for processo in psutil.process_iter(['pid', 'name']):
    
    if processo.info['name'] == "Code.exe":
        Aberto = True

        horas = 0
        minutos = 0
        segundos = 0
        data = str( date.today() )

        while Aberto:
            
            with open(Dados, 'r',encoding='utf-8') as arquivo:
                dados = json.load(arquivo)    
                dados["Tempo"] = (f"{horas}h {minutos}m {segundos}s")
                dados["Data"] = (str(data))
                    
            with open(Dados, "w") as f:
                json.dump(dados, f)
                    
            
            if processo.info['name'] == "Code.exe": # verificar se o vscode tá aberto
                time.sleep(1)
                segundos += 1
                print(f"\rAberto por {horas}h {minutos}m {segundos}s", end="")

                if segundos == 60: # minutos
                    segundos = 0
                    minutos += 1
                    
                
                if minutos == 60: # hora
                    minutos = 0
                    horas += 1
                
        break

