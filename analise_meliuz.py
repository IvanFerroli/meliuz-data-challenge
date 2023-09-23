import pandas as pd
from consultas import consulta_lojas_categorias, consulta_variacao_lojas

df = pd.read_csv('./dados_meliuz.csv')

quantidade_lojas = consulta_lojas_categorias.contar_lojas(df)
quantidade_categorias = consulta_lojas_categorias.contar_categorias(df)
media_conversao = consulta_lojas_categorias.media_conversao(df)
media_taxa_confirmacao = consulta_lojas_categorias.media_taxa_confirmacao(df)

print(f'Quantidade de Lojas: {quantidade_lojas}')
print(f'Quantidade de Categorias: {quantidade_categorias}')
print(f'Média de Conversão: {media_conversao}')
print(f'Média de Taxa de Confirmação: {media_taxa_confirmacao}')


