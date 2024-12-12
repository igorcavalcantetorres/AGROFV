import numpy as np
import pandas as pd
from datetime import date, timedelta, datetime

# Caminho do arquivo de entrada
caminho_do_arquivo_1 = r'C:\Users\igorc\Documents\GitProjetos\AGROFV\CR10X_12-61.DAT'
dados = pd.read_csv(caminho_do_arquivo_1, sep=',', header=[0])

#Substituir valores negativos por 0 em todo o DataFrame
#dados[dados < 0.9] = 0

#Salvar o DataFrame atualizado em um arquivo .dat
#dados.to_csv(r'C:\Users\i5\Documents\GitProjetos\AGROFV\CR10X_SAF_1_sem_negativos.dat', sep=',', index=False)

