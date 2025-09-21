import pandas as pd
import locale
from datetime import datetime

# Define o local para interpretar meses em português
locale.setlocale(locale.LC_TIME, "pt_BR.utf8")  

# Carrega o arquivo Excel
arquivo_entrada = "tabelas.xlsx"  
sheet_name = "Planilha1"  

df = pd.read_excel(arquivo_entrada, sheet_name=sheet_name)

# Converte a coluna 'mês' para datetime
def converter_mes_ano(data):
    try:
        return datetime.strptime(data, "%B/%Y")
    except ValueError:
        return pd.NaT  # Retorna NaT se a conversão falhar

df['mês'] = df['mês'].apply(converter_mes_ano)

# Remove valores inválidos e ordena
df = df.dropna(subset=['mês']).sort_values(by='mês').reset_index(drop=True)

# Lista para armazenar os DataFrames organizados
tabelas = {}

# Obtém combinações únicas de 'dado' e 'tipo'
combinacoes = df[['dado', 'tipo']].drop_duplicates()

for _, (dado, tipo) in combinacoes.iterrows():
    # Filtra os dados para a combinação específica
    df_filtrado = df[(df['dado'] == dado) & (df['tipo'] == tipo)]

    # Seleciona e reorganiza as colunas
    df_final = df_filtrado[['mês', 't0-1', 't0', 't0+1', 't0+2']]

    # Armazena no dicionário
    tabelas[f"{dado} - {tipo}"] = df_final

# Salva todas as tabelas em um único arquivo Excel
arquivo_saida = "tabelas_organizadas.xlsx"
with pd.ExcelWriter(arquivo_saida) as writer:
    for nome_aba, tabela in tabelas.items():
        tabela.to_excel(writer, sheet_name=nome_aba[:31], index=False)  # Limita a 31 caracteres

print(f"Processo concluído! Arquivo '{arquivo_saida}' gerado com todas as tabelas organizadas.")

