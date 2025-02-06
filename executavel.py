import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
import csv
import time
from matplotlib.ticker import MaxNLocator

caminho_do_arquivo_1 = r'C:\Users\i5\Documents\GitProjetos\AGROFV\CR10X_SAF_1.dat'
dados = pd.read_csv(caminho_do_arquivo_1, sep=',', header=[0]) 
coluna_2=dados['h']
    
bloco=1440

ano = 2024  

dias_julianos = np.arange(63, 150)

def calcular_data_do_dia_juliano(ano, d):
 
    is_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        
    dias_por_mes = [31, 28 + is_bissexto, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    mes = 0
    while d > dias_por_mes[mes]:
        d -= dias_por_mes[mes]
        mes += 1
       
    return date(ano, mes + 1, d)

resultados = []


for dia_juliano in dias_julianos:

    if dia_juliano < 1 or dia_juliano > 366 or (dia_juliano == 366 and not ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))):
        print(f"Dia juliano {dia_juliano} inválido para o ano {ano}!")
    else:
      
        data = calcular_data_do_dia_juliano(ano, dia_juliano)
               
    for minuto in range(0, 24 * 60): 
          
            hora_completa = datetime.combine(data, datetime.min.time()) + timedelta(minutes=minuto)
            hora = hora_completa.strftime('%H:%M')
            resultados.append([dia_juliano, data.strftime('%d/%m/%Y'), hora])

irradiacao=dados['f']
temperatura=dados['g']
data_frame=pd.DataFrame(resultados, columns=["Dia Juliano","Data","Hora"])
data_frame["Irradiacao"]=irradiacao
data_frame["Temperatura"]=temperatura
data_frame.to_csv(r'C:\Users\i5\Documents\GitProjetos\AGROFV\resultados.csv', index=False, sep=',', header=True)

for i in range(0, len(data_frame), bloco):
    plt.figure(figsize=(12, 8))
    
    # Subplot 1: Gráfico de Irradiação
    plt.subplot(2, 1, 1)  # 2 linhas, 1 coluna, primeiro gráfico
    plt.plot(data_frame['Hora'][i:i+bloco], data_frame['Irradiacao'][i:i+bloco], color='blue')
    legenda = data_frame['Data'][i] 
    plt.legend([f'Dia {legenda}'], loc='upper left')
    plt.xlabel('Hora')
    plt.ylabel('Irradiação - W/m²')
    plt.title(f'Irradiação do dia {data_frame["Data"][i]}')
    plt.xticks(rotation=45)  # Rotacionar os rótulos para melhor visualização
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=24))
    
    # Subplot 2: Gráfico de Temperatura
    plt.subplot(2, 1, 2)  # 2 linhas, 1 coluna, segundo gráfico
    plt.plot(data_frame['Hora'][i:i+bloco], data_frame['Temperatura'][i:i+bloco], color='red')
    plt.legend([f'Dia {legenda}'], loc='upper left')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura - °C')
    plt.title(f'Temperatura do dia {data_frame["Data"][i]}')
    plt.xticks(rotation=45)  # Rotacionar os rótulos para melhor visualização
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=24))
   
    # Ajustando o layout para evitar sobreposição
    plt.tight_layout()
    plt.show()

    # Pausando por 2 segundos antes de exibir o próximo gráfico
    time.sleep(2)
        
 