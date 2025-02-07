def processar_arquivo(nome_arquivo):
    # Abre o arquivo de entrada no modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # Verifica se o arquivo tem pelo menos 1440 linhas
    if len(linhas) != 1440:
        print(f"O arquivo {nome_arquivo} não contém 1440 linhas.")
        return

    # Exclui as 330 primeiras linhas e as linhas após a 780ª
    linhas_filtradas = linhas[330:1110]  # da linha 331 até a linha 1110 (inclusive)

    # Cria o novo nome de arquivo com o mesmo nome de entrada
    nome_arquivo_saida = nome_arquivo

    # Salva as linhas filtradas no novo arquivo
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        arquivo_saida.writelines(linhas_filtradas)

    print(f"Arquivo processado com sucesso e salvo como {nome_arquivo_saida}.")

# Exemplo de uso
nome_arquivo_entrada = "dia_273_2022.dat"  # Substitua pelo nome do seu arquivo
processar_arquivo(nome_arquivo_entrada)