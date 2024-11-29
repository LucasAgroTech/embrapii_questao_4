import pandas as pd

def load_and_prepare_data(file_path):
    """
    Carrega e prepara os dados para análise.

    Parâmetros:
        file_path (str): Caminho para o arquivo de dados.

    Retorna:
        pd.DataFrame: DataFrame com os dados preparados.
    """
    # Carregar o arquivo Excel
    data = pd.ExcelFile(file_path)
    df_dados = data.parse('dados')

    # Garantir que 'ano' e 'mes' estão como inteiros
    df_dados['ano'] = df_dados['ano'].astype(int)
    df_dados['mes'] = df_dados['mes'].astype(int)

    # Criar a coluna 'data' para representar o tempo
    df_dados['data'] = pd.to_datetime({
        'year': df_dados['ano'],
        'month': df_dados['mes'],
        'day': 1
    })

    # Configurar a coluna 'data' como índice e remover as colunas redundantes
    df_dados.set_index('data', inplace=True)
    df_dados.drop(columns=['ano', 'mes'], inplace=True)

    return df_dados
