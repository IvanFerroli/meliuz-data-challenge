import pandas as pd
from src.relatorios import relatorio_lojas_categorias


def contar_lojas(df):
    quantidade_lojas = df['Parceiro'].nunique()
    return quantidade_lojas

def contar_categorias(df):
    quantidade_categorias = df['Categoria'].nunique()
    return quantidade_categorias

def media_conversao(df):
    df['Conversao'] = df['Nº de vendas'] / df['Qtd de acessos']
    media_conversao = df['Conversao'].mean()
    return media_conversao

def media_taxa_confirmacao(df):
    df['Taxa de Confirmação'] = df['Nº de vendas confirmadas'] / df['Nº de vendas']
    media_taxa_confirmacao = df['Taxa de Confirmação'].mean()
    return media_taxa_confirmacao

import pandas as pd

def gmv_total_por_mes_categoria(df):
    df['Data'] = pd.to_datetime(df['Data'])
    
    df['Ano-Mês'] = df['Data'].dt.strftime('%Y-%m')
    
    gmv_por_categoria_mes = df.groupby(['Categoria', 'Ano-Mês'])['GMV'].sum()
    
    return gmv_por_categoria_mes




