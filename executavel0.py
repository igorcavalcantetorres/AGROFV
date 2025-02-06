# Função para dividir o arquivo .DAT em arquivos menores
def dividir_arquivo(input_file, linhas_por_arquivo=1440):
    # Lê o arquivo .DAT
    with open(input_file, 'r') as f:
        # Lê todas as linhas do arquivo
        linhas = f.readlines()

    # Extraímos o cabeçalho (primeira linha)
    cabecalho = linhas[0]

    # Contamos o total de dados sem o cabeçalho
    dados = linhas[1:]

    # Calcula quantos arquivos serão criados
    total_linhas = len(dados)
    total_arquivos = total_linhas // linhas_por_arquivo + (1 if total_linhas % linhas_por_arquivo != 0 else 0)

    # Dividindo e escrevendo os dados em novos arquivos
    for i in range(total_arquivos):
        # Definir o nome do novo arquivo
        output_file = f'dia_{i+337}_2022.DAT'

        # Pega o índice de início e fim para os dados que serão escritos neste arquivo
        inicio = i * linhas_por_arquivo
        fim = (i + 1) * linhas_por_arquivo

        # Pega o bloco de dados que será escrito neste arquivo
        bloco_dados = dados[inicio:fim]

        # Escreve o cabeçalho + o bloco de dados no novo arquivo
        with open(output_file, 'w') as f_out:
            f_out.write(cabecalho)  # Escreve o cabeçalho
            f_out.writelines(bloco_dados)  # Escreve o bloco de dados

# Nome do arquivo .DAT original
input_file = 'CR10X_337-365.DAT'

# Chama a função para dividir o arquivo
dividir_arquivo(input_file)