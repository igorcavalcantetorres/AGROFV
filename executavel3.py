import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo de entrada
caminho_do_arquivo_1 = r'C:\Users\igorc\Documents\GitProjetos\AGROFV\estudo_final.txt'
dados = pd.read_csv(caminho_do_arquivo_1, sep=',', header=[0])

print(dados)

# Variáveis
meses = dados['Meses']
irradiacao = dados['Irradiacao']
temperatura = dados['Temperatura_amb_media']
temp_cell = dados['Temperatura_cel_media']
interceptada = dados['Irradiacao_coletada']
energia = dados['Energia']
produtividade = dados['Produtividade']
fc=dados['FC']
pr=dados['PR']

#Script para criação do gráfico de energia e irradiação solar
def plot_bar_with_trend(bar_data, line_data, x_labels, xlabel, bar_ylabel, line_ylabel):
    fig, ax1 = plt.subplots(figsize=(9,4))

    ax1.bar(x_labels, bar_data.values, color='gray', edgecolor='black')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    ax2 = ax1.twinx()  # Segundo eixo Y
    ax2.plot(x_labels, line_data.values, color='red', linewidth=2, linestyle='--')
    ax2.set_ylabel(line_ylabel, color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    ax1.set_xticks(range(len(x_labels)))
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')  # Rotação com alinhamento à direita

    plt.tight_layout()
    plt.show()


# Gráfico 1: Energia (barras) e Irradiação (linha)
plot_bar_with_trend(
    energia, 
    irradiacao, 
    meses,  # Usar os meses como rótulos no eixo X
    'Months', 
    'Energy (kWh)', 
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

def plot_bar_with_two_trends(bar_data, trend1_data, trend2_data, x_labels, xlabel, bar_ylabel, trend1_ylabel, trend2_ylabel):
    fig, ax1 = plt.subplots(figsize=(8, 4))

    # Gráfico de barras (Variável principal)
    ax1.bar(x_labels, bar_data.values, color='gray', edgecolor='gray', label='Energia (kWh)')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    # Gráfico de linhas (Primeira linha de tendência)
    ax2 = ax1.twinx()  # Segundo eixo Y
    ax2.plot(x_labels, trend1_data.values, color='red', linewidth=2, linestyle='--', label='Temperatura Ambiente (°C)')
    ax2.plot(x_labels, trend2_data.values, color='green', linewidth=2, linestyle='-', label='Temperatura da Célula (°C)')
    ax2.set_ylabel(f'{trend1_ylabel}', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    # Adicionar legendas
    legend=fig.legend(loc='upper right', bbox_to_anchor=(1, 1.01), bbox_transform=ax1.transAxes, fontsize=7.2)
    legend.get_frame().set_linewidth(0)

    # Rotacionar os rótulos do eixo X
    ax1.set_xticks(range(len(x_labels)))
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')

    # Ajustar layout
    plt.tight_layout()
    plt.show()

# Chamando a função para criar o gráfico
plot_bar_with_two_trends(
    energia, 
    temperatura, 
    temp_cell, 
    meses, 
    'Months', 
    'Energy (kWh)', 
    'Temperature (°C)', 
    'Temperature (°C)'
)


def plot_bar_with_two_trends_v2(bar_data, bar1_data, bar2_data, x_labels, xlabel, bar_ylabel, bar1_ylabel, bar2_ylabel):
    fig, ax1 = plt.subplots(figsize=(8, 4))

    bar_width = 0.3  # Largura das barras
    x = np.arange(len(x_labels))  # Posições no eixo X

    # Gráfico de barras (Variável principal) - Ajuste para barras lado a lado
    ax1.bar(x - bar_width, bar_data.values, width=bar_width, color='gray', edgecolor='gray', label='Productivity Yeld')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='black')
    ax1.tick_params(axis='y', labelcolor='black')

    # Gráfico de barras (Primeira linha de tendência)
    ax2 = ax1.twinx()  # Segundo eixo Y
    ax2.bar(x, bar1_data.values, width=bar_width, color='red', label='PR')
    ax2.bar(x + bar_width, bar2_data.values, width=bar_width, color='green', label='CF')
    ax2.set_ylabel(f'{bar1_ylabel} / {bar2_ylabel}', color='black')
    ax2.tick_params(axis='y', labelcolor='black')

    # Adicionar legendas
    legend = fig.legend(loc='upper right', bbox_to_anchor=(1, 1.01), bbox_transform=ax1.transAxes, fontsize=7.2)
    legend.get_frame().set_linewidth(0)

    # Rotacionar os rótulos do eixo X
    ax1.set_xticks(x)
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')

    # Ajustar layout
    plt.tight_layout()
    plt.show()

# Chamando a função para criar o gráfico
plot_bar_with_two_trends_v2(
    produtividade, 
    pr, 
    fc, 
    meses, 
    'Months', 
    'Productivity Yeld (kWh/kwp)', 
    'PR (%)', 
    'CF (%)'
)