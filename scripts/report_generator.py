from fpdf import FPDF
import os
from datetime import datetime

class PDFReport(FPDF):
    def header(self):
        # Caminho para a logo
        logo_path = 'logo.png'  # Substitua pelo caminho correto da sua logo

        # Inserir a logo se existir
        if os.path.exists(logo_path):
            self.image(logo_path, x=20, y=10, w=20)  # Ajuste x, y e w conforme necessário
            x_position = 20 + 20 + 10  # x + largura da logo + espaçamento
            epw_title = self.epw - 30  # epw - largura da logo - espaçamento
        else:
            x_position = self.l_margin
            epw_title = self.epw

        # Definir posição para o título
        self.set_xy(x_position, 10)
        self.set_font('Helvetica', 'B', 15)
        self.set_text_color(0, 0, 0)  # Preto para o texto
        self.cell(epw_title, 10, 'Relatório de Projeções da Embrapii para 2025', ln=False, align='L')
        self.ln(10)

        # Linha abaixo do cabeçalho
        self.set_draw_color(200, 200, 200)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(5)

    def footer(self):
        # Posicionar o rodapé a 15 mm do fim da página
        self.set_y(-15)
        self.set_draw_color(200, 200, 200)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(5)

        # Definir fonte para o rodapé
        self.set_font('Helvetica', 'I', 10)
        
        # Inserir a data à esquerda
        date_str = datetime.now().strftime('%d/%m/%Y')
        self.cell(self.epw / 2, 10, date_str, align='L')

        # Inserir número da página no centro
        page_no = f'Página {self.page_no()}'
        page_no_width = self.get_string_width(page_no) + 6  # Adicionar um pouco de espaçamento
        self.set_x((self.w - page_no_width) / 2)
        self.cell(page_no_width, 10, page_no, align='C')

def generate_pdf_report():
    """
    Gera um relatório em PDF com os gráficos e explicações.
    """
    # Criar diretório para o relatório, se não existir
    os.makedirs('reports', exist_ok=True)

    pdf = PDFReport(format='A4')
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.alias_nb_pages()

    # Definir margens antes de adicionar a página
    pdf.set_left_margin(20)
    pdf.set_right_margin(20)
    pdf.epw = pdf.w - pdf.l_margin - pdf.r_margin  # Largura efetiva da página

    pdf.add_page()

    # Definir estilos de fonte
    font_title = ('Helvetica', 'B', 14)
    font_subtitle = ('Helvetica', 'B', 12)
    font_text = ('Helvetica', '', 11)
    font_italic = ('Helvetica', 'I', 11)

    # Introdução
    pdf.set_font(*font_text)
    introducao = (
        "Este relatório apresenta as projeções para os indicadores da Embrapii em 2025.\n\n"
        "Utilizamos o método de Suavização Exponencial Holt-Winters para realizar as previsões com base nos dados históricos disponíveis."
    )
    pdf.multi_cell(pdf.epw, 8, introducao)
    pdf.ln(5)

    # Metodologia
    pdf.set_font(*font_title)
    pdf.set_text_color(0, 102, 204)  # Azul para o título
    pdf.cell(pdf.epw, 10, 'Metodologia', ln=True)
    pdf.ln(2)
    pdf.set_font(*font_text)
    pdf.set_text_color(0, 0, 0)  # Preto para o texto
    metodologia = (
        "A Suavização Exponencial Holt-Winters é um método que considera tendências e sazonalidades nos dados. "
        "Foi escolhido por sua adequação aos dados disponíveis e pela capacidade de capturar padrões sazonais."
    )
    pdf.multi_cell(pdf.epw, 8, metodologia)
    pdf.ln(5)

    # Resultados e Gráficos
    pdf.set_font(*font_title)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(pdf.epw, 10, 'Resultados e Projeções', ln=True)
    pdf.ln(2)
    pdf.set_text_color(0, 0, 0)

    indicators = {
        'novos_projetos_contratados': 'Novos Projetos Contratados',
        'valor_projetos_contratados': 'Valor Total dos Projetos Contratados',
        'projetos_concluidos': 'Projetos Concluídos'
    }

    for indicator_key, indicator_name in indicators.items():
        # Subtítulo
        pdf.set_font(*font_subtitle)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(pdf.epw, 10, f'Projeção para {indicator_name}', ln=True)
        pdf.ln(2)
        pdf.set_font(*font_text)
        pdf.set_text_color(80, 80, 80)
        
        # Texto explicativo
        texto = (
            f"A projeção para {indicator_name} em 2025 indica um crescimento esperado, seguindo a tendência observada nos anos anteriores."
        )
        pdf.multi_cell(pdf.epw, 8, texto)
        pdf.ln(2)

        # Inserir o gráfico correspondente
        image_path = f'figures/projecao_{indicator_key}.png'
        if os.path.exists(image_path):
            # Verificar se a imagem cabe na página atual; senão, adicionar uma nova página
            if pdf.get_y() + 85 > pdf.page_break_trigger:
                pdf.add_page()
            pdf.image(image_path, x=pdf.l_margin, w=pdf.epw)
            pdf.ln(5)
        else:
            pdf.set_font(*font_italic)
            pdf.cell(pdf.epw, 10, f"Imagem {image_path} não encontrada.", ln=True)
            pdf.ln(5)

        # Linha divisória entre seções
        pdf.set_draw_color(200, 200, 200)
        pdf.ln(2)
        pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
        pdf.ln(5)

    # Conclusão
    pdf.set_font(*font_title)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(pdf.epw, 10, 'Conclusão', ln=True)
    pdf.ln(2)
    pdf.set_font(*font_text)
    pdf.set_text_color(0, 0, 0)
    conclusao = (
        "Com base nas projeções, espera-se que os indicadores da Embrapii continuem a crescer em 2025. "
        "Recomenda-se considerar esses resultados no planejamento estratégico."
    )
    pdf.multi_cell(pdf.epw, 8, conclusao)
    pdf.ln(5)

    # Salvar o PDF
    pdf.output('reports/relatorio_previsoes_2025.pdf')
