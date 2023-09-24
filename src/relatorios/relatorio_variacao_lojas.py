import pandas as pd

def gerar_relatorio_variacao_lojas(df):
    
    max_vendas = df.groupby('Parceiro')['Nº de vendas'].max()

    max_vendas_categoria = df.groupby(['Categoria', 'Parceiro'])['Nº de vendas'].max()
    min_vendas_categoria = df.groupby(['Categoria', 'Parceiro'])['Nº de vendas'].min()

    acoes_promocionais = df[df['Tipo'] == 'Promocional']
    total_vendas_acoes_promocionais = acoes_promocionais['Nº de vendas'].sum()
    total_vendas = df['Nº de vendas'].sum()
    representatividade = (total_vendas_acoes_promocionais / total_vendas) * 100

    relatorio_path = './relatórios/relatorio_variacao_lojas.csv'
    
    resultado = pd.DataFrame({
        'Maior Pico de Vendas': max_vendas,
        'Maior Vendas por Categoria': max_vendas_categoria,
        'Menor Vendas por Categoria': min_vendas_categoria,
        'Representatividade de Ações Promocionais': [representatividade]
    })

    resultado.to_csv(relatorio_path, index=False)
