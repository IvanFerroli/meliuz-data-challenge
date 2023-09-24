import pandas as pd

def gerar_relatorio_lojas_categorias(df):
    
    gmv_por_categoria = df.groupby('Categoria')['GMV'].sum()

    dia_maior_pico = df[df.groupby('Parceiro')['Nº de vendas'].transform(max) == df['Nº de vendas']]['Data']

    max_vendas_categoria = df.groupby(['Categoria', 'Parceiro'])['Nº de vendas'].max()
    min_vendas_categoria = df.groupby(['Categoria', 'Parceiro'])['Nº de vendas'].min()

    acoes_promocionais = df[df['Tipo'] == 'Promocional']
    total_vendas_acoes_promocionais = acoes_promocionais['Nº de vendas'].sum()
    total_vendas = df['Nº de vendas'].sum()
    representatividade = (total_vendas_acoes_promocionais / total_vendas) * 100

    relatorio_path = './relatórios/relatorio_lojas_categorias.csv'
    
    resultado = pd.DataFrame({
        'GMV Total por Categoria': gmv_por_categoria,
        'Dia com Maior Pico de Vendas por Parceiro': dia_maior_pico,
        'Maior Vendas por Categoria e Parceiro': max_vendas_categoria,
        'Menor Vendas por Categoria e Parceiro': min_vendas_categoria,
        'Representatividade de Ações Promocionais': [representatividade]
    })

    resultado.to_csv(relatorio_path, index=False)
