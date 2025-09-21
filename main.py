# import pdfplumber
# import pandas as pd
# import os
# from glob import glob
#
# # Pasta onde os PDFs estão armazenados
# pasta_pdfs = "C:/Users/tjrgi/Desktop/PrismaFiscal/"
#
# # Lista de arquivos PDF na pasta
# arquivos_pdfs = glob(os.path.join(pasta_pdfs, "relatorio_mensal_*.pdf"))
#
# # Lista para armazenar os DataFrames das cinco tabelas
# tabelas_compiladas = [pd.DataFrame() for _ in range(5)]
#
# # Percorre cada PDF
# for pdf_path in arquivos_pdfs:
#     with pdfplumber.open(pdf_path) as pdf:
#         first_page = pdf.pages[0]  # Obtém a primeira página
#         tables = first_page.extract_tables()  # Extrai todas as tabelas
#
#     # Converte e adiciona as tabelas ao compilado
#     for i in range(min(len(tables), 5)):  # Garante que não exceda 5 tabelas
#         df = pd.DataFrame(tables[i])  # Converte para DataFrame
#         df["Arquivo"] = os.path.basename(pdf_path)  # Adiciona coluna identificando a origem
#         tabelas_compiladas[i] = pd.concat([tabelas_compiladas[i], df], ignore_index=True)
#
# # Salva os DataFrames em arquivos Excel
# for i, df in enumerate(tabelas_compiladas):
#     nome_arquivo = f"tabela_{i+1}.xlsx"
#     df.to_excel(nome_arquivo, index=False)
#
# print("Processo concluído! Arquivos Excel gerados.")
#
