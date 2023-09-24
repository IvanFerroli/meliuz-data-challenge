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
