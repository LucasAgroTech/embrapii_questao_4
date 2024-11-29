from scripts.data_preparation import load_and_prepare_data
from scripts.forecasting import forecast_indicators
from scripts.visualization import plot_projections
from scripts.report_generator import generate_pdf_report

def main():
    # Caminho do arquivo de dados
    file_path = 'data/raw/embrapii_dados.xlsx'

    # Carregar e preparar os dados
    df_dados = load_and_prepare_data(file_path)

    # Realizar as projeções
    projections_df, models = forecast_indicators(df_dados)

    # Visualizar e salvar as projeções
    plot_projections(df_dados, projections_df)

    # Salvar as projeções
    projections_df.to_csv('data/projections/projecoes_2025.csv')

    # Gerar o relatório em PDF
    generate_pdf_report()

if __name__ == "__main__":
    main()
