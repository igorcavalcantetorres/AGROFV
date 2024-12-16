import numpy as np
import pandas as pd
from datetime import date, timedelta, datetime

# Caminho do arquivo de entrada
caminho_do_arquivo_1 = r'C:\Users\i5\Documents\GitProjetos\AGROFV\CR10X_12-61.DAT'
dados = pd.read_csv(caminho_do_arquivo_1, sep=',', header=[0])

#Substituir valores negativos por 0 em todo o DataFrame
#dados[dados < 0.9] = 0

#Salvar o DataFrame atualizado em um arquivo .dat
#dados.to_csv(r'C:\Users\i5\Documents\GitProjetos\AGROFV\CR10X_SAF_1_sem_negativos.dat', sep=',', index=False)

# Definindo a coluna de irradiação
irradiacao = dados['f']

# Bloco de 1440 registros
bloco = 1440

# Ano e dias julianos
ano = 2023
dias_julianos = np.arange(12, 62)

# Função para calcular a data a partir do dia juliano
def calcular_data_do_dia_juliano(ano, d):
    is_bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    dias_por_mes = [31, 28 + is_bissexto, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = 0
    while d > dias_por_mes[mes]:
        d -= dias_por_mes[mes]
        mes += 1
    return date(ano, mes + 1, d)

# Lista para armazenar os resultados
somas_por_bloco = []
dias_julianos_por_bloco = []
bloco_atual = []

# Iteração para calcular a soma da irradiação em blocos de 1440
for i, valor in enumerate(irradiacao):
    bloco_atual.append(valor)  # Adiciona o valor atual ao bloco
    if (i + 1) % bloco == 0 or i == len(irradiacao) - 1:  # A cada 1440 iterações ou no último valor
        soma_bloco = sum(bloco_atual)/60/1000  # Converte a soma para kWh/m²
        somas_por_bloco.append(soma_bloco)
        bloco_atual = []  # Reinicia o bloco
        
        # Determina o dia juliano correspondente ao bloco
        dia_juliano = dias_julianos[len(somas_por_bloco) - 1] if len(somas_por_bloco) <= len(dias_julianos) else None
        dias_julianos_por_bloco.append(dia_juliano)

# Criação de um DataFrame para armazenar os resultados
data_frame_somas = pd.DataFrame({
    'Dia_Juliano': dias_julianos_por_bloco,
    'Soma_Irradiacao_kWh': somas_por_bloco
})

data_frame_somas['Data'] = data_frame_somas['Dia_Juliano'].apply(lambda x: calcular_data_do_dia_juliano(ano, x).strftime('%d/%m/%Y'))

# Exibição e salvamento do resultado
print(data_frame_somas)
data_frame_somas.to_csv('somas_irradiacao_dia_juliano.csv', index=False)