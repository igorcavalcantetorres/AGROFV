import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from datetime import date, timedelta, datetime
import csv

caminho_do_arquivo_1 = r'C:\Users\i5\Documents\GitProjetos\AGROFV\CR10X_SAF_1.dat'
dados = pd.read_csv(caminho_do_arquivo_1, sep=',', header=[0]) 
coluna_2=dados['h']
    
bloco=1440

ano = 2024  # Ano de exemplo, você pode alterar conforme necessário

dias_julianos = np.arange(63, 150)

def calcular_data_do_dia_juliano(ano, d):
    # Verificar se o ano é bissexto
    is_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    
    # Lista com o número de dias de cada mês
    dias_por_mes = [31, 28 + is_bissexto, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Inicializa o mês e o dia
    mes = 0
    while d > dias_por_mes[mes]:
        d -= dias_por_mes[mes]
        mes += 1
    
    # Retorna a data correspondente
    return date(ano, mes + 1, d)

# Parâmetros de entrada
# Lista para armazenar os resultados
resultados = []

# Gerar a lista de dias julianos e horas de 1 em 1 minuto
for dia_juliano in dias_julianos:
    # Verificar se o dia juliano é válido
    if dia_juliano < 1 or dia_juliano > 366 or (dia_juliano == 366 and not ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0))):
        print(f"Dia juliano {dia_juliano} inválido para o ano {ano}!")
    else:
        # Calcular a data correspondente ao dia juliano
        data = calcular_data_do_dia_juliano(ano, dia_juliano)
        
    for minuto in range(0, 24 * 60):  # 24 horas * 60 minutos
            # Criando o objeto datetime para o dia e hora exatos
            hora_completa = datetime.combine(data, datetime.min.time()) + timedelta(minutes=minuto)
            # Formatando a hora no formato HH:MM
            hora = hora_completa.strftime('%H:%M')
            resultados.append([dia_juliano, data, hora])

irradiacao=dados['f']
temperatura=dados['g']
data_frame=pd.DataFrame(resultados, columns=["Dia Juliano","Data","Hora"])
data_frame["Irradiacao"]=irradiacao
data_frame["Temperatura"]=temperatura
data_frame.to_csv(r'C:\Users\i5\Documents\GitProjetos\AGROFV\resultados.csv', index=False, sep=',', header=True)

plt.plot(data_frame['Hora'], data_frame['Irradiacao'], color='blue')
plt.title('Irradiação x Hora')
plt.xlabel('Tempo')
plt.ylabel('Irradiação - W/m²')
plt.show()