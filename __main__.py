import time
import json
import psutil
from datetime import date, datetime

arquivoJson = "C:\\Users\\cassi\\TempoCodando\\Informações.json"  
horas = 0
minutos = 0
segundos = 0

tempoAtual = datetime.now().time()
horaAtual = tempoAtual.strftime("%H:%M:%S")
print(horaAtual)

diaNumero = date.today().weekday()
diasSemana = ["Seg","Ter","Qua","Qui","Sex","Sab","Dom"]
diaAtual = diasSemana[diaNumero]

while ( "Code.exe" in ((Janela).name() for Janela in psutil.process_iter()) ):
        
    with open(arquivoJson, 'r') as arquivo:
        lendoArquivo = json.load(arquivo)
        lendoArquivo[f"{diaAtual}"] = (f"{horas}h {minutos}m {segundos}s")
        
                    
    with open(arquivoJson, "w") as escrevendoArquivo:
        json.dump(lendoArquivo, escrevendoArquivo)
                    
    time.sleep(1)
    segundos += 1
    print(f"\rAberto por {horas}h {minutos}m {segundos}s", end="")

    if segundos == 60: 
        segundos = 0
        minutos += 1
    

    if minutos == 60:
        minutos = 0
        horas += 1