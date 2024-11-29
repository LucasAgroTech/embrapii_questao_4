import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing

def forecast_indicators(df_dados, steps=12):
    """
    Realiza projeções dos indicadores utilizando Holt-Winters.

    Parâmetros:
        df_dados (pd.DataFrame): Dados históricos dos indicadores.
        steps (int): Número de períodos para projetar.

    Retorna:
        tuple: DataFrame com as projeções e dicionário com os modelos.
    """
    projections = {}
    models = {}

    # Aplicar o método Holt-Winters para cada indicador
    for column in df_dados.columns:
        model = ExponentialSmoothing(
            df_dados[column],
            seasonal='add',
            seasonal_periods=12
        ).fit()
        models[column] = model
        projections[column] = model.forecast(steps=steps)

    # Converter as projeções em um DataFrame
    projections_df = pd.DataFrame(projections)
    projections_df.index = pd.date_range(
        start=df_dados.index[-1] + pd.DateOffset(months=1),
        periods=steps,
        freq='MS'
    )

    return projections_df, models
