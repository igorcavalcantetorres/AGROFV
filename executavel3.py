import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo de entrada
caminho_do_arquivo_1 = r'C:\Users\i5\Documents\GitProjetos\AGROFV\final.txt'
dados = pd.read_csv(caminho_do_arquivo_1, sep=',', header=[0])

print(dados)

# Variáveis
meses = dados['Meses']
irradiacao = dados['Irradiacao']
interceptada = dados['Irradiacao_coletada']
energia = dados['Energia']
produtividade = dados['Produtividade']
fc=dados['FC']
pr=dados['PR']

# Função para criar o gráfico de barras com linha de tendência
def plot_bar_with_trend(bar_data, line_data, x_labels, xlabel, bar_ylabel, line_ylabel):
    fig, ax1 = plt.subplots()

    # Gráfico de barras (Variável principal)
    ax1.bar(x_labels, bar_data.values, color='skyblue', edgecolor='black')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Gráfico de linha (Linha de tendência)
    ax2 = ax1.twinx()  # Segundo eixo Y
    ax2.plot(x_labels, line_data.values, color='red', linewidth=2, linestyle='--')
    ax2.set_ylabel(line_ylabel, color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Rotacionar os rótulos do eixo X
    ax1.set_xticks(range(len(x_labels)))
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')  # Rotação com alinhamento à direita

    # Ajustar layout
    plt.tight_layout()
    plt.show()


# Gráfico 1: Energia (barras) e Irradiação (linha)
plot_bar_with_trend(
    energia, 
    irradiacao, 
    meses,  # Usar os meses como rótulos no eixo X
    'Months', 
    'Energy (kwh)', 
    'Solar Irradiation (kWh/m²)'

)

def plot_bar_with_trend(bar_data, x_labels, xlabel, bar_ylabel):
    fig, ax1 = plt.subplots()

    # Gráfico de barras (Variável principal)
    ax1.bar(x_labels, bar_data.values, color='skyblue', edgecolor='black')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Rotacionar os rótulos do eixo X
    ax1.set_xticks(range(len(x_labels)))
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')  # Rotação com alinhamento à direita

    # Ajustar layout
    plt.tight_layout()
    plt.show()

# Gráfico 1: Energia (barras) e Irradiação (linha)
plot_bar_with_trend(
    interceptada, 
    meses,  # Usar os meses como rótulos no eixo X
    'Months', 
    'Intercepted energy (kWh)',     

)

# Função para criar o gráfico de barras com linha de tendência
def plot_bar_with_trend(bar_data, line_data, x_labels, xlabel, bar_ylabel, line_ylabel):
    fig, ax1 = plt.subplots()

    # Gráfico de barras (Variável principal)
    ax1.bar(x_labels, bar_data.values, color='skyblue', edgecolor='black')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Gráfico de linha (Linha de tendência)
    ax2 = ax1.twinx()  # Segundo eixo Y
    ax2.plot(x_labels, line_data.values, color='red', linewidth=2, linestyle='--')
    ax2.set_ylabel(line_ylabel, color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Rotacionar os rótulos do eixo X
    ax1.set_xticks(range(len(x_labels)))
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')  # Rotação com alinhamento à direita

    # Ajustar layout
    plt.tight_layout()
    plt.show()


# Gráfico 1: Energia (barras) e Irradiação (linha)
plot_bar_with_trend(
    produtividade, 
    irradiacao, 
    meses,  # Usar os meses como rótulos no eixo X
    'Months', 
    'Productivity Yeld (kWh/kwp)', 
    'Solar Irradiation (kWh/m²)'

)

# Função para criar o gráfico de barras com linha de tendência
def plot_bar_with_trend(bar_data, line_data, x_labels, xlabel, bar_ylabel, line_ylabel):
    fig, ax1 = plt.subplots()

    # Gráfico de barras (Variável principal)
    ax1.bar(x_labels, bar_data.values, color='skyblue', edgecolor='black')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Gráfico de linha (Linha de tendência)
    ax2 = ax1.twinx()  # Segundo eixo Y
    ax2.plot(x_labels, line_data.values, color='red', linewidth=2, linestyle='--')
    ax2.set_ylabel(line_ylabel, color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    # Rotacionar os rótulos do eixo X
    ax1.set_xticks(range(len(x_labels)))
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')  # Rotação com alinhamento à direita

    # Ajustar layout
    plt.tight_layout()
    plt.show()


# Gráfico 1: Energia (barras) e Irradiação (linha)
plot_bar_with_trend(
    fc, 
    energia, 
    meses,  # Usar os meses como rótulos no eixo X
    'Months', 
    'Capacity Factor (%)', 
    'Energy (kWh)'

)