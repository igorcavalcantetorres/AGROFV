import os

def processar_arquivo(nome_arquivo_entrada, numero_arquivo_saida):
    # Abre o arquivo de entrada no modo de leitura
    with open(nome_arquivo_entrada, 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Verifica se o arquivo tem pelo menos 1440 linhas
    if len(linhas) != 1441:
        print(f"O arquivo {nome_arquivo_entrada} não contém 1441 linhas.")
        return

    # Mantém a primeira linha (cabeçalho) e as 780 linhas subsequentes após a linha 330
    cabecalho = linhas[0]  # A primeira linha é o cabeçalho
    linhas_dados = linhas[1:]  # As outras linhas são os dados

    # Exclui as 330 primeiras linhas de dados e mantém as 780 seguintes
    linhas_filtradas = linhas_dados[330:1080]

    # Junta o cabeçalho com as linhas filtradas
    linhas_finais = [cabecalho] + linhas_filtradas

    # Cria o nome do arquivo de saída com base no número fornecido
    nome_arquivo_saida = f"dia_{numero_arquivo_saida}_2023.DAT"
    
    # Salva as linhas filtradas no novo arquivo com o nome gerado
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.writelines(linhas_finais)

    print(f"Arquivo {nome_arquivo_saida} processado com sucesso.")

def processar_arquivos_em_sequencia(diretorio_entrada, diretorio_saida):
    # Verifica se o diretório de saída existe, se não, cria
    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    # Processa os arquivos de 1 a 365
    for numero_arquivo in range(14, 366):
        nome_arquivo_entrada = os.path.join(diretorio_entrada, f"dia_{numero_arquivo}_2023.DAT")
        nome_arquivo_saida = os.path.join(diretorio_saida, f"dia_{numero_arquivo}_2023.DAT")
        
        if os.path.exists(nome_arquivo_entrada):
            processar_arquivo(nome_arquivo_entrada, numero_arquivo)
        else:
            print(f"Arquivo {nome_arquivo_entrada} não encontrado.")

# Defina o diretório de entrada e saída
diretorio_entrada = r"C:\Users\igorc\Documents\GitProjetos\AGROFV\Dias_2023"
diretorio_saida = r"C:\Users\igorc\Documents\GitProjetos\AGROFV\Dias_2023\saida"

# Processa os arquivos de 1 a 365
processar_arquivos_em_sequencia(diretorio_entrada, diretorio_saida)