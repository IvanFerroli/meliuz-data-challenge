import pandas as pd

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
