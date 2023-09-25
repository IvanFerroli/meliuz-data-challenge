import pandas as pd
from src.relatorios import relatorio_variacao_lojas


def maior_pico_vendas(df):
    max_vendas = df.groupby('Parceiro')['Nº de vendas'].max()
    return max_vendas

def melhor_pior_desempenho(df):
    max_vendas = df.groupby(['Categoria', 'Parceiro'])['Nº de vendas'].max()
    min_vendas = df.groupby(['Categoria', 'Parceiro'])['Nº de vendas'].min()
    return max_vendas, min_vendas

def representatividade_acoes_promocionais(df):
    acoes_promocionais = df[df['Tipo'] == 'Promocional']
    total_vendas_acoes_promocionais = acoes_promocionais['Nº de vendas'].sum()
    total_vendas = df['Nº de vendas'].sum()
    representatividade = (total_vendas_acoes_promocionais / total_vendas) * 100
    return representatividade
    
def calcular_conversao_media(df):
    df['Conversao'] = df['Nº de vendas'] / df['Qtd de acessos']
    conversao_media = df.groupby('Parceiro')['Conversao'].mean()
    return conversao_media

def calcular_taxa_confirmacao_media(df):
    df['Taxa de Confirmação'] = df['Nº de vendas confirmadas'] / df['Nº de vendas']
    taxa_confirmacao_media = df.groupby('Parceiro')['Taxa de Confirmação'].mean()
    return taxa_confirmacao_media

import pandas as pd

def lojas_com_desvios_significativos(df):
    media_historica = df.groupby('Parceiro')['Nº de vendas'].mean()
    
    limiar_desvio = media_historica.std() * 2
    
    lojas_com_desvios = media_historica[abs(df.groupby('Parceiro')['Nº de vendas'].max() - media_historica) > limiar_desvio]
    
    return lojas_com_desvios

import pandas as pd

def dia_maior_pico_vendas(df):
    idx = df.groupby('Parceiro')['Nº de vendas'].idxmax()
    
    dias_maior_pico = df.loc[idx, ['Parceiro', 'Data']]
    
    return dias_maior_pico

