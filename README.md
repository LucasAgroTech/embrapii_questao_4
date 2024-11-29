
# Embrapii Projeções 2025

![Logo da Embrapii](logo.png)

## Índice

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Uso](#uso)
  - [Preparação dos Dados](#preparação-dos-dados)
  - [Execução do Script](#execução-do-script)
  - [Visualização dos Resultados](#visualização-dos-resultados)
- [Personalização](#personalização)
- [Resolução de Problemas](#resolução-de-problemas)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Visão Geral

O **Embrapii Projeções 2025** é uma aplicação Python projetada para gerar relatórios detalhados em PDF que apresentam projeções de indicadores-chave para a Embrapii em 2025. Utilizando técnicas avançadas de previsão, como a Suavização Exponencial Holt-Winters, a aplicação processa dados históricos, gera projeções futuras, cria visualizações gráficas e compila todas as informações em um relatório profissional e personalizado.

## Recursos

- **Preparação de Dados**: Carregamento e limpeza de dados históricos a partir de arquivos Excel.
- **Projeção de Indicadores**: Utilização do método Holt-Winters para previsão de tendências e sazonalidades.
- **Visualização Gráfica**: Geração de gráficos que combinam dados históricos e projeções.
- **Geração de Relatórios em PDF**: Criação de um relatório bem formatado com introdução, metodologia, resultados, gráficos, conclusão, logo da Embrapii, data e numeração de páginas.
- **Personalização**: Inclusão de logotipo personalizado e ajustes de layout para margens consistentes.

## Pré-requisitos

Antes de iniciar, certifique-se de ter os seguintes itens instalados:

- **Python 3.7 ou superior**
- **pip** (gerenciador de pacotes do Python)

## Instalação

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/LucasAgroTech/embrapii_questao_4.git
   cd embrapii_questao_4
   ```

2. **Crie um Ambiente Virtual (Opcional, mas Recomendado)**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as Dependências**

   Certifique-se de que o arquivo `requirements.txt` está presente no diretório raiz e contém todas as bibliotecas necessárias.

   ```bash
   pip install -r requirements.txt
   ```

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

```
embrapii_questao_4/
│
├── data/
│   ├── raw/
│   │   └── embrapii_dados.xlsx
│   ├── processed/
│   └── projections/
│       └── projecoes_2025.csv
│
├── figures/
│   ├── historic/
│   │   ├── historico_novos_projetos_contratados.png
│   │   ├── historico_valor_projetos_contratados.png
│   │   └── historico_projetos_concluidos.png
│   ├── projecao_novos_projetos_contratados.png
│   ├── projecao_valor_projetos_contratados.png
│   └── projecao_projetos_concluidos.png
│
├── reports/
│   └── relatorio_previsoes_2025.pdf
│
├── scripts/
│   ├── data_preparation.py
│   ├── forecasting.py
│   ├── visualization.py
│   └── report_generator.py
│
├── main.py
├── requirements.txt
├── README.md
└── logo.png
```

## Uso

### Preparação dos Dados

1. **Adicionar Dados Históricos**

   Coloque o arquivo de dados históricos da Embrapii no diretório `data/raw/` com o nome `embrapii_dados.xlsx`. Certifique-se de que o arquivo esteja formatado corretamente, com colunas representando os indicadores e linhas representando períodos (por exemplo, meses).

### Execução do Script

1. **Execute o Script Principal**

   No diretório raiz do projeto, execute:

   ```bash
   python main.py
   ```

   Este comando realizará as seguintes ações:

   - **Carregamento e Preparação dos Dados**: Carrega os dados brutos e os prepara para análise.
   - **Geração das Projeções**: Utiliza o método Holt-Winters para prever os indicadores para 2025.
   - **Criação dos Gráficos**: Gera gráficos que combinam dados históricos e projeções.
   - **Geração do Relatório em PDF**: Compila todas as informações e gráficos em um relatório profissional.

### Visualização dos Resultados

- **Gráficos Gerados**

  Os gráficos gerados estão localizados em `figures/` e `figures/historic/`. Cada gráfico está nomeado de acordo com o indicador correspondente.

- **Relatório em PDF**

  O relatório final pode ser encontrado em `reports/relatorio_previsoes_2025.pdf`. Abra-o para visualizar todas as seções, incluindo introdução, metodologia, resultados com gráficos e conclusão.

## Personalização

### Inserir uma Logo Personalizada

1. **Substitua a Logo**

   - **Arquivo de Logo**: Certifique-se de que o arquivo de logo está no formato PNG e nomeado como `logo.png`.
   - **Posicionamento e Tamanho**: No arquivo `report_generator.py`, ajuste os parâmetros `x`, `y` e `w` na função `self.image()` para posicionar e dimensionar a logo conforme desejado.

     ```python
     self.image(logo_path, x=20, y=10, w=20)  # Ajuste x, y e w conforme necessário
     ```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para aprimorar esta aplicação.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
