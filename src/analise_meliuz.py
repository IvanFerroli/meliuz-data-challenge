import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.insert(0, project_dir)

import pandas as pd
from src.consultas import consulta_lojas_categorias, consulta_variacao_lojas


def main():
    df = pd.read_csv('./dados_meliuz.csv')

    quantidade_lojas = consulta_lojas_categorias.contar_lojas(df)
    quantidade_categorias = consulta_lojas_categorias.contar_categorias(df)
    media_conversao = consulta_lojas_categorias.media_conversao(df)
    media_taxa_confirmacao = consulta_lojas_categorias.media_taxa_confirmacao(df)

    print(f'Quantidade de Lojas: {quantidade_lojas}')
    print(f'Quantidade de Categorias: {quantidade_categorias}')
    print(f'Média de Conversão: {media_conversao}')
    print(f'Média de Taxa de Confirmação: {media_taxa_confirmacao}')

    max_vendas = consulta_variacao_lojas.maior_pico_vendas(df)
    max_vendas_categoria, min_vendas_categoria = consulta_variacao_lojas.melhor_pior_desempenho(df)
    representatividade_acoes_promocionais = consulta_variacao_lojas.representatividade_acoes_promocionais(df)

    print(f'Maior Pico de Vendas: {max_vendas}')
    print(f'Melhor Desempenho por Categoria: {max_vendas_categoria}')
    print(f'Pior Desempenho por Categoria: {min_vendas_categoria}')
    print(f'Representatividade de Ações Promocionais: {representatividade_acoes_promocionais}')

if __name__ == "__main__":
    main()
