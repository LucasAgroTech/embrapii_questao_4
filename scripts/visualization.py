import matplotlib.pyplot as plt
import os

def plot_indicators(df_dados):
    """
    Plota os indicadores históricos.

    Parâmetros:
        df_dados (pd.DataFrame): Dados históricos dos indicadores.
    """
    df_dados.plot(subplots=True, figsize=(10, 8), title="Indicadores Históricos da Embrapii")
    plt.tight_layout()
    plt.show()

def plot_projections(df_dados, projections_df):
    """
    Plota as projeções junto com os dados históricos.

    Parâmetros:
        df_dados (pd.DataFrame): Dados históricos dos indicadores.
        projections_df (pd.DataFrame): Projeções dos indicadores.
    """
    # Criar o diretório 'figures/' se não existir
    os.makedirs('figures', exist_ok=True)
    
    for column in df_dados.columns:
        plt.figure(figsize=(10, 5))
        plt.plot(df_dados[column], label='Histórico')
        plt.plot(projections_df[column], label='Projeção 2025', linestyle='--')
        plt.title(f'Projeção para {column}')
        plt.legend()
        plt.tight_layout()
        
        # Salvar o gráfico
        filename = f'figures/projecao_{column}.png'
        plt.savefig(filename)
        plt.close()
