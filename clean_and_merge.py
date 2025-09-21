import pandas as pd

# Número de tabelas que foram salvas
num_tabelas = 5

# Dicionário para armazenar os DataFrames processados
tabelas_filtradas = {}

# Processa cada arquivo Excel
for i in range(1, num_tabelas + 1):
    # Carrega a planilha
    nome_arquivo = f"tabela_{i}.xlsx"
    df = pd.read_excel(nome_arquivo)

    dados = df

    # Lista para armazenar os dados processados
    linhas_filtradas = []

    # Percorre o DataFrame em blocos de 8 linhas
    for j in range(0, len(dados), 8):
        bloco = dados.iloc[j:j+8]  # Pega o bloco de 8 linhas
        if len(bloco) >= 8:  # Garante que há pelo menos 8 linhas para processar
            linhas_filtradas.append(bloco.iloc[3:])  # Mantém apenas as últimas 5 linhas

    # Concatena os blocos processados
    df_final = pd.concat(linhas_filtradas, ignore_index=True)

    # Armazena o DataFrame processado
    tabelas_filtradas[f"Tabela_{i}"] = df_final

# Salva todas as tabelas em um único arquivo Excel com múltiplas abas
with pd.ExcelWriter("tabelas_compiladas.xlsx") as writer:
    for nome_aba, df in tabelas_filtradas.items():
        df.to_excel(writer, sheet_name=nome_aba, index=False)

print("Processo concluído! Arquivo 'tabelas_compiladas.xlsx' gerado com todas as tabelas filtradas.")
