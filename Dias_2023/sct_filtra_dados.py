def processar_arquivo(nome_arquivo):
    # Abre o arquivo de entrada no modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Verifica se o arquivo tem pelo menos 1440 linhas
    if len(linhas) != 1441:
        print(f"O arquivo {nome_arquivo} não contém 1440 linhas.")
        return

    # Mantém a primeira linha (cabeçalho) e as 780 linhas subsequentes após a linha 330
    cabecalho = linhas[0]  # A primeira linha é o cabeçalho
    linhas_dados = linhas[1:]  # As outras linhas são os dados

    # Exclui as 330 primeiras linhas de dados e mantém as 780 seguintes
    linhas_filtradas = linhas_dados[330:1080]

    # Junta o cabeçalho com as linhas filtradas
    linhas_finais = [cabecalho] + linhas_filtradas

    # Salva as linhas filtradas no novo arquivo com o mesmo nome de entrada
    with open(nome_arquivo, 'w') as arquivo_saida:
        arquivo_saida.writelines(linhas_finais)

    print(f"Arquivo processado com sucesso e salvo como {nome_arquivo}.")


nome_arquivo_entrada = r"C:\Users\igorc\Documents\GitProjetos\AGROFV\Dias_2023\dia_20_2023.DAT"
processar_arquivo(nome_arquivo_entrada)