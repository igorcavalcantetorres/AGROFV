import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Caminho do arquivo de entrada
caminho_do_arquivo_1 = r'C:\Users\i5\Documents\GitProjetos\AGROFV\estudo_final.txt'
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
eficiencia=dados['Eficiencia']*100

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
def plot_bar_with_separate_secondary_axes(bar_data, temp_data, eff_data, x_labels, xlabel, bar_ylabel, temp_ylabel, eff_ylabel):
    fig, ax1 = plt.subplots(figsize=(8, 4))

    # Configuração do eixo X e largura das barras
    bar_width = 0.4
    x = np.arange(len(x_labels))

    # Gráfico de barras (Eixo Y primário)
    ax1.bar(x, bar_data, width=bar_width, color='gray', edgecolor='black', label='Intercepted Radiation')
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(bar_ylabel, color='gray')
    ax1.tick_params(axis='y', labelcolor='gray')

    # Configuração do eixo secundário (Temperatura)
    ax2 = ax1.twinx()
    ax2.spines.right.set_position(('outward', 10))  # Posiciona o terceiro eixo para fora
    ax2.plot(x, temp_data, color='red', marker='o', label='Temperature (°C)')
    ax2.set_ylabel(temp_ylabel, color='red')
    ax2.yaxis.set_ticks_position('right')  # Garante que os ticks fiquem no lado direito
    ax2.yaxis.set_label_position('right')  # Garante que o label fique no lado direito
    ax2.tick_params(axis='y', labelcolor='red')  # Move os ticks do eixo de temperatura para fora
    
    ax2.spines['right'].set_visible(True)
    
    # Adicionando um terceiro eixo para eficiência
    ax3 = ax1.twinx()
    ax3.spines.right.set_position(('outward', 50))  # Posiciona o terceiro eixo para fora
    ax3.plot(x, eff_data, color='green', marker='s', label='Efficiency (%)')
    ax3.set_ylabel(eff_ylabel, color='green')
    ax3.tick_params(axis='y', labelcolor='green')  # Move os ticks do eixo de eficiência para fora
    
    # Ajuste para evitar sobreposição
    

    # Configurando rótulos do eixo X
    ax1.set_xticks(x)
    ax1.set_xticklabels(x_labels, rotation=45, ha='right')

    # Adicionando legendas
    fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3, fontsize=8)

    # Ajustar layout
    plt.tight_layout()
    plt.show()

# Chamando a função para criar o gráfico
plot_bar_with_separate_secondary_axes(
    interceptada, 
    temp_cell,
    eficiencia,
    meses, 
    'Months', 
    'Intercepted Radiation (kWh)', 
    'Temperature (°C)', 
    'Efficiency (%)'
)