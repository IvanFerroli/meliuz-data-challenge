import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.insert(0, project_dir)

import pandas as pd
from src.consultas import consulta_lojas_categorias, consulta_variacao_lojas

def gerar_relatorio_completo(df):
    quantidade_lojas = consulta_lojas_categorias.contar_lojas(df)
    quantidade_categorias = consulta_lojas_categorias.contar_categorias(df)
    media_conversao = consulta_lojas_categorias.media_conversao(df)
    media_conversao_periodo = consulta_variacao_lojas.calcular_conversao_media(df)
    media_confirmacao_periodo = consulta_variacao_lojas.calcular_taxa_confirmacao_media(df)
    media_taxa_confirmacao = consulta_lojas_categorias.media_taxa_confirmacao(df)
    desvios_significativos = consulta_variacao_lojas.lojas_com_desvios_significativos(df)
    max_vendas = consulta_variacao_lojas.maior_pico_vendas(df)
    max_vendas_categoria, min_vendas_categoria = consulta_variacao_lojas.melhor_pior_desempenho(df)
    representatividade_acoes_promocionais = consulta_variacao_lojas.representatividade_acoes_promocionais(df)
    gmvs_por_categoria_mes = consulta_lojas_categorias.gmv_total_por_mes_categoria(df)
    dia_maior_pico_vendas = consulta_variacao_lojas.dia_maior_pico_vendas(df)

    resultado = {
        'Quantidade de Lojas': [quantidade_lojas],
        'Quantidade de Categorias': [quantidade_categorias],
        'Média de Conversão': [media_conversao],
        'Média de Conversão por Loja': [media_conversao_periodo],
        'Média de Taxa de Confirmação por Loja': [media_confirmacao_periodo],
        'Média de Taxa de Confirmação': [media_taxa_confirmacao],
        'Lojas com Desvios Significativos': [desvios_significativos],
        'Maior Pico de Vendas': [max_vendas],
        'Melhor Desempenho por Categoria': [max_vendas_categoria],
        'Pior Desempenho por Categoria': [min_vendas_categoria],
        'Representatividade de Ações Promocionais': [representatividade_acoes_promocionais],
        'GMV Total por Categoria e Mês': [gmvs_por_categoria_mes],
        'Dia com Maior Pico de Vendas': [dia_maior_pico_vendas]
    }

    df_resultado = pd.DataFrame(resultado)

    df_resultado.to_csv('./relatorios/relatorio_completo.csv', index=False)

def main():
    df = pd.read_csv('./dados_meliuz.csv')
    gerar_relatorio_completo(df)

if __name__ == "__main__":
    main()
