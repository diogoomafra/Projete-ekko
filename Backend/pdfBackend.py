#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PDF Completo - Tecnologias do Backend (EKKO)
Versão detalhada com diagramas e exemplos de código
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor, black, white, grey
from datetime import datetime

def criar_pdf_completo():
    # Configuração do documento
    filename = "Backend.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilos personalizados para página inicial
    main_title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontSize=36,
        spaceAfter=20,
        alignment=TA_CENTER,
        textColor=HexColor('#1B4332'),
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor('#2D6A4F'),
        fontName='Helvetica'
    )
    
    doc_title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=15,
        alignment=TA_CENTER,
        textColor=HexColor('#1B4332'),
        fontName='Helvetica-Bold'
    )
    
    doc_subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=40,
        alignment=TA_CENTER,
        textColor=HexColor('#40916C'),
        fontName='Helvetica'
    )
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=28,
        spaceAfter=30,
        alignment=TA_CENTER,
        textColor=HexColor("#032512")
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=20,
        textColor=HexColor("#000000")
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=8,
        spaceBefore=15,
        textColor=HexColor("#000000")
    )
    
    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=6,
        spaceBefore=10,
        textColor=HexColor("#000000")
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['Normal'],
        fontSize=8,
        fontName='Courier',
        backColor=HexColor('#F5F5F5'),
        leftIndent=20,
        rightIndent=20,
        spaceAfter=10,
        spaceBefore=5
    )
    
    bullet_style = ParagraphStyle(
        'Bullet',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        spaceAfter=4
    )
    
    # Conteúdo do documento
    story = []
    
    # Página de título acadêmica
    story.append(Spacer(1, 80))
    
    # Título principal com destaque
    story.append(Paragraph("EKKO", main_title_style))
    story.append(Paragraph("Dashboard que promove a agricultura de precisão", subtitle_style))
    
    # Linha decorativa
    story.append(HRFlowable(width="50%", thickness=2, color=HexColor('#2D6A4F'), 
                           spaceBefore=20, spaceAfter=20, hAlign='CENTER'))
    
    # Título do documento
    story.append(Paragraph("Documentação Técnica do Backend", doc_title_style))
    story.append(Paragraph("Tecnologias, Arquitetura e Implementação", doc_subtitle_style))
    
    # Informações institucionais
    story.append(Spacer(1, 60))
    
    # Tabela de informações acadêmicas
    info_data = [
        ["", ""],
        ["Instituição:", "Escola Técnica de Eletrônica 'FMC'"],
        ["Curso:", "Desenvolvimento de Sistemas"],
        ["Equipe:", "34DS08"],
        ["Evento:", "45ª Projete - Fraternidade e Ecologia Integral"],
        ["Área:", "Tecnologia e Agricultura de Precisão"],
        ["", ""]
    ]
    
    info_table = Table(info_data, colWidths=[1.5*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (0, -2), 'Helvetica-Bold'),
        ('FONTNAME', (1, 1), (1, -2), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 1), (0, -2), HexColor('#2D6A4F')),
        ('TEXTCOLOR', (1, 1), (1, -2), HexColor('#52796F')),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 30),
    ]))
    story.append(info_table)
    
    # Rodapé da página inicial
    story.append(Spacer(1, 80))
    
    # Data de geração
    data_atual = datetime.now().strftime("%d de %B de %Y")
    meses = {
        'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
        'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
        'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
        'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
    }
    for eng, pt in meses.items():
        data_atual = data_atual.replace(eng, pt)
    
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_CENTER,
        textColor=grey,
        fontName='Helvetica-Oblique'
    )
    
    story.append(HRFlowable(width="30%", thickness=1, color=grey, 
                           spaceBefore=10, spaceAfter=15, hAlign='CENTER'))
    story.append(Paragraph(f"Documento gerado em {data_atual}", date_style))
    
    # Resumo executivo na primeira página
    story.append(Spacer(1, 40))
    
    resumo_style = ParagraphStyle(
        'Resumo',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        textColor=HexColor('#2D6A4F'),
        fontName='Helvetica',
        leftIndent=40,
        rightIndent=40,
        borderWidth=1,
        borderColor=HexColor('#95D5B2'),
        borderPadding=15,
        backColor=HexColor('#F8FFF9')
    )
    
    story.append(Paragraph("<b>Resumo Executivo</b>", ParagraphStyle(
        'ResumoTitle', parent=resumo_style, fontSize=12, fontName='Helvetica-Bold',
        alignment=TA_CENTER, spaceAfter=10
    )))
    
    story.append(Paragraph(
        "Este documento apresenta a arquitetura técnica completa do backend do sistema EKKO, "
        "uma solução inovadora que integra agricultura de precisão com gamificação educativa. "
        "O projeto combina tecnologias modernas como FastAPI, MongoDB Atlas, inteligência artificial "
        "via Llama 3.2, e técnicas avançadas de processamento de dados para criar uma plataforma "
        "robusta de análise de solo e assistência agrícola inteligente.",
        resumo_style
    ))
    
    story.append(PageBreak())
    
    # Página de dedicatória
    story.append(Spacer(1, 200))
    
    dedicatoria_style = ParagraphStyle(
        'Dedicatoria',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_CENTER,
        textColor=HexColor('#2D6A4F'),
        fontName='Helvetica-Oblique',
        spaceAfter=10
    )
    
    story.append(Paragraph(
        "<i>\"A agricultura não é apenas sobre cultivar alimentos,<br/>"
        "é sobre cultivar o futuro.\"</i>",
        dedicatoria_style
    ))
    
    story.append(Spacer(1, 40))
    
    story.append(Paragraph(
        "Dedicado aos agricultores brasileiros que,<br/>"
        "com sua dedicação e conhecimento,<br/>"
        "alimentam nossa nação.",
        ParagraphStyle('DedicatoriaText', parent=dedicatoria_style, 
                      fontSize=11, textColor=HexColor('#52796F'))
    ))
    
    story.append(PageBreak())
    
    # Índice
    story.append(Paragraph("Índice", heading1_style))
    indice_data = [
        ["1.", "Visão Geral do Projeto", "3"],
        ["2.", "Framework Web & API", "4"],
        ["3.", "Banco de Dados", "5"],
        ["4.", "Inteligência Artificial", "6"],
        ["5.", "Sistema de Análise de Solo", "8"],
        ["6.", "Busca e Recuperação (RAG)", "9"],
        ["7.", "APIs Externas", "10"],
        ["8.", "Endpoints da API", "11"],
        ["9.", "Configuração e Deploy", "12"],
        ["10.", "Performance e Otimização", "13"],
        ["11.", "Estrutura do Código", "14"],
        ["12.", "Exemplos de Implementação", "15"]
    ]
    
    indice_table = Table(indice_data, colWidths=[0.5*inch, 4*inch, 0.5*inch])
    indice_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(indice_table)
    
    story.append(PageBreak())
    
    # 1. Visão Geral
    story.append(Paragraph("1. Visão Geral do Projeto", heading1_style))
    
    story.append(Paragraph("Objetivo", heading2_style))
    story.append(Paragraph(
        "O projeto Ekko, desenvolvido pela equipe 3408, do curso ”Desenvolvimento de Sistemas“, alinhado à proposta da Projete "
        "de fraternidade e ecologia integral, consiste em um website no qual o agricultor pode acessar dados e feedbacks "
        "relacionados ao solo de sua região de plantio, junto à análises produzidas por IA, suporte de um ChatBot treinado com "
        "fontes renomadas do setor agrícola brasileiro, estatísticas, gráficos, mapas de calor e mais. "
        "Além disso, o grupo também desenvolveu uma simulação gamificada que permite ao usuário entender de que maneira o dispositivo "
        "móvel Ekko, ou 'carrinho', encarregado de coletar os valores do parâmetros do solo, como pH, umidade, temperatura, NPK e outros, "
        "funcionaria na prática, por meio da coleta e transmissão de dados em determinada região de plantio.",
        normal_style
    ))

    story.append(Paragraph("Componentes Principais", heading2_style))
    componentes_data = [
        ["Componente", "Tecnologia", "Função"],
        ["Frontend", "HTML5, CSS3, JavaScript", "Desenvolvimento do website"],
        ["Backend", "Python + FastAPI", "API REST e processamento de dados"],
        ["Banco de Dados", "MongoDB Atlas", "Armazenamento de dados na nuvem"],
        ["Chatbot", "Llama 3.2 + Ollama", "Assistente agrícola inteligente"],
        ["Análise de Solo", "Python + IA", "Avaliação de 12 parâmetros do solo"],
        ["Busca RAG", "FAISS + Transformers", "Recuperação de conhecimento agrícola"]
    ]
    
    componentes_table = Table(componentes_data, colWidths=[1.5*inch, 2*inch, 2.5*inch])
    componentes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(componentes_table)
    
    story.append(PageBreak())
    
    # 2. Framework Web & API
    story.append(Paragraph("2. Framework Web & API", heading1_style))
    
    story.append(Paragraph("FastAPI 0.104.1", heading2_style))
    story.append(Paragraph(
        "<b>FastAPI</b> é um framework web moderno e de alta performance para construção de APIs "
        "com Python 3.7+, baseado em type hints padrão do Python.", normal_style
    ))
    
    story.append(Paragraph("Características Principais:", heading3_style))
    story.append(Paragraph("• <b>Performance:</b> Uma das mais rápidas disponíveis, comparável ao NodeJS e Go", bullet_style))
    story.append(Paragraph("• <b>Documentação Automática:</b> Gera automaticamente documentação interativa (Swagger UI)", bullet_style))
    story.append(Paragraph("• <b>Validação:</b> Validação automática de dados baseada em Python type hints", bullet_style))
    story.append(Paragraph("• <b>Async/Await:</b> Suporte nativo para programação assíncrona", bullet_style))
    
    story.append(Paragraph("Exemplo de Implementação:", heading3_style))
    story.append(Paragraph(
        "@app.post(\"/unity/soil/save/{unity_id}\")<br/>"
        "def save_soil(unity_id: str, soil: SoilData):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Validação automática via Pydantic<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;if not unity_profiles.find_one({\"_id\": unity_id}):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raise HTTPException(status_code=404)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Processamento dos dados<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;soil_doc = {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"unity_id\": unity_id,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"timestamp\": datetime.utcnow(),<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"soil_parameters\": {...}<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;}<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;return unity_soil_data.insert_one(soil_doc)", code_style
    ))
    
    story.append(Paragraph("Pydantic 2.5.0", heading2_style))
    story.append(Paragraph(
        "Biblioteca para validação de dados usando Python type annotations. "
        "Garante que os dados recebidos estejam no formato correto.", normal_style
    ))
    
    story.append(Paragraph("Modelo de Dados do Solo:", heading3_style))
    story.append(Paragraph(
        "class SoilData(BaseModel):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;session_id: str<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;ph: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;umidade: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;temperatura: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;salinidade: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;condutividade: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;nitrogenio: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;fosforo: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;potassio: float<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Validação automática de tipos", code_style
    ))
    
    story.append(PageBreak())
    
    # 3. Banco de Dados
    story.append(Paragraph("3. Banco de Dados", heading1_style))
    
    story.append(Paragraph("MongoDB Atlas", heading2_style))
    story.append(Paragraph(
        "Banco de dados NoSQL na nuvem que oferece escalabilidade automática, "
        "backup e replicação. Ideal para dados semi-estruturados como perfis de usuários "
        "e dados de sensores.", normal_style
    ))
    
    story.append(Paragraph("Estrutura das Collections:", heading3_style))
    
    # Tabela de collections
    collections_data = [
        ["Collection", "Propósito", "Documentos Típicos"],
        ["Python_userData", "Perfis dos agricultores", "~100-1000 usuários"],
        ["Unity_soilData", "Dados de solo da simulação", "~10000+ registros"],
    ]
    
    collections_table = Table(collections_data, colWidths=[2*inch, 2.5*inch, 1.5*inch])
    collections_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(collections_table)
    
    story.append(Paragraph("Exemplo de Documento - Perfil do Usuário:", heading3_style))
    story.append(Paragraph(
        "{<br/>"
        "&nbsp;&nbsp;\"_id\": \"unity_bf87c29494e0\",<br/>"
        "&nbsp;&nbsp;\"dados_pessoais\": {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"nome\": \"João Silva\",<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"email\": \"joao@fazenda.com\",<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"telefone\": \"(35) 99999-9999\"<br/>"
        "&nbsp;&nbsp;},<br/>"
        "&nbsp;&nbsp;\"propriedade\": {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"nome\": \"Fazenda Esperança\",<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"area_hectares\": 120.5,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"cultivos_principais\": [\"Café\", \"Milho\"],<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"regiao\": \"Sul de Minas Gerais\"<br/>"
        "&nbsp;&nbsp;},<br/>"
        "&nbsp;&nbsp;\"unity_stats\": {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"total_sessions\": 15,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"best_score\": 850<br/>"
        "&nbsp;&nbsp;}<br/>"
        "}", code_style
    ))
    
    story.append(Paragraph("SQLite - Memória Local", heading2_style))
    story.append(Paragraph(
        "Usado para armazenar a memória de longo prazo do chatbot. Permite que o sistema "
        "lembre de informações específicas sobre cada usuário entre sessões.", normal_style
    ))
    
    story.append(PageBreak())
    
    # 4. Inteligência Artificial
    story.append(Paragraph("4. Inteligência Artificial", heading1_style))
    
    story.append(Paragraph("Ollama + Llama 3.2", heading2_style))
    story.append(Paragraph(
        "<b>Ollama</b> é uma ferramenta que permite executar modelos de linguagem grandes "
        "localmente. O <b>Llama 3.2</b> é um modelo de IA desenvolvido pela Meta, "
        "otimizado para conversação e tarefas de texto.", normal_style
    ))
    
    story.append(Paragraph("Vantagens da Execução Local:", heading3_style))
    story.append(Paragraph("• <b>Privacidade:</b> Dados não saem do servidor local", bullet_style))
    story.append(Paragraph("• <b>Custo:</b> Sem taxas por token/requisição", bullet_style))
    story.append(Paragraph("• <b>Controle:</b> Parâmetros totalmente configuráveis", bullet_style))
    story.append(Paragraph("• <b>Latência:</b> Respostas mais rápidas (sem rede externa)", bullet_style))
    
    story.append(Paragraph("Configuração do Modelo:", heading3_style))
    story.append(Paragraph(
        "MODEL_OPTIONS = {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"num_predict\": 500,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Máximo de tokens por resposta<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"temperature\": 0.7,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Criatividade (0.0-1.0)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"top_p\": 0.9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Consistência (0.0-1.0)<br/>"
        "}<br/><br/>"
        "# Configuração de timeout e retry<br/>"
        "STREAM_TIMEOUT = 120&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 2 minutos para streaming<br/>"
        "MAX_RETRIES = 3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Tentativas em caso de falha", code_style
    ))
    
    story.append(Paragraph("Sentence Transformers", heading2_style))
    story.append(Paragraph(
        "Biblioteca especializada em criar embeddings (representações vetoriais) de texto. "
        "Usado para converter documentos e consultas em vetores numéricos para busca semântica.", normal_style
    ))
    
    story.append(Paragraph("Modelo Utilizado: all-MiniLM-L6-v2", heading3_style))
    story.append(Paragraph("• <b>Dimensões:</b> 384 (cada texto vira um vetor de 384 números)", bullet_style))
    story.append(Paragraph("• <b>Idiomas:</b> Suporte a português e outros idiomas", bullet_style))
    story.append(Paragraph("• <b>Performance:</b> Balanceio entre qualidade e velocidade", bullet_style))
    story.append(Paragraph("• <b>Tamanho:</b> ~90MB (modelo compacto)", bullet_style))
    
    story.append(Paragraph("FAISS (Facebook AI Similarity Search)", heading2_style))
    story.append(Paragraph(
        "Biblioteca otimizada para busca de similaridade em grandes volumes de vetores. "
        "Permite encontrar rapidamente os documentos mais relevantes para uma consulta.", normal_style
    ))
    
    story.append(Paragraph("Implementação da Busca RAG:", heading3_style))
    story.append(Paragraph(
        "def local_database_search(query: str) -> str:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Converte a consulta em vetor<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;query_embedding = embedding_model.encode([query])<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Busca os 3 documentos mais similares<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;_, indices = index.search(<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;np.array(query_embedding, dtype=np.float32), 3<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Retorna os trechos encontrados<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;context = \"\\n---\\n\".join([documents[i] for i in indices[0]])<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;return f\"Resultados: {context}\"", code_style
    ))
    
    story.append(PageBreak())
    
    # 5. Sistema de Análise de Solo
    story.append(Paragraph("5. Sistema de Análise de Solo", heading1_style))
    
    story.append(Paragraph("Parâmetros Analisados", heading2_style))
    
    # Tabela de parâmetros
    parametros_data = [
        ["Parâmetro", "Faixa Ideal", "Unidade", "Importância"],
        ["pH do Solo", "6.0 - 7.0", "-", "Disponibilidade de nutrientes"],
        ["Umidade", "40 - 70", "%", "Absorção de água pelas plantas"],
        ["Temperatura", "20 - 30", "°C", "Atividade microbiana e raízes"],
        ["Salinidade", "≤ 600", "ppm", "Estresse osmótico das plantas"],
        ["Condutividade", "≤ 1.5", "dS/m", "Concentração de sais"],
        ["Nitrogênio (N)", "20 - 100", "mg/kg", "Crescimento vegetativo"],
        ["Fósforo (P)", "15 - 50", "mg/kg", "Desenvolvimento radicular"],
        ["Potássio (K)", "100 - 250", "mg/kg", "Resistência e qualidade"],
        ["Drenagem", "60 - 90", "%", "Aeração das raízes"],
        ["Aeração", "10 - 30", "%", "Respiração radicular"],
        ["Compactação", "≤ 2.0", "g/cm³", "Penetração das raízes"],
        ["Ativ. Microbiana", "≥ 50", "mg CO2/kg", "Ciclagem de nutrientes"]
    ]
    
    parametros_table = Table(parametros_data, colWidths=[1.3*inch, 0.8*inch, 0.6*inch, 1.8*inch])
    parametros_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(parametros_table)
    
    story.append(Paragraph("Sistema de Classificação", heading2_style))
    
    # Tabela de status
    status_data = [
        ["Status", "Descrição", "Ação Recomendada"],
        ["Ideal", "Parâmetro dentro da faixa ótima", "Manter práticas atuais"],
        ["Atenção", "Próximo do ideal, requer monitoramento", "Ajustes preventivos"],
        ["Crítico", "Fora da faixa, ação imediata necessária", "Correção urgente"]
    ]
    
    status_table = Table(status_data, colWidths=[1*inch, 2.5*inch, 2*inch])
    status_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(status_table)
    
    story.append(Paragraph("Algoritmo de Análise:", heading3_style))
    story.append(Paragraph(
        "def analyze_parameter(param_name, value):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;ranges = SOIL_RANGES[param_name]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;status = determine_status(param_name, value, ranges)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;return {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"valor\": value,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"faixa_ideal\": get_ideal_range_text(ranges),<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"status\": status,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"impacto\": MESSAGES[param_name][status],<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"sugestao\": get_suggestion(param_name, value, status)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;}", code_style
    ))
    
    story.append(PageBreak())
    
    # 6. APIs Externas
    story.append(Paragraph("6. APIs Externas", heading1_style))
    
    story.append(Paragraph("INMET - Instituto Nacional de Meteorologia", heading2_style))
    story.append(Paragraph(
        "API oficial do governo brasileiro para dados meteorológicos. Fornece previsões "
        "precisas e atualizadas para todo o território nacional.", normal_style
    ))
    
    story.append(Paragraph("Implementação:", heading3_style))
    story.append(Paragraph(
        "def get_inmet_forecast(lat: float, lon: float) -> str:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Encontra estação mais próxima<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;closest_station = find_closest_station(lat, lon)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;station_code = closest_station['CD_ESTACAO']<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Consulta API do INMET<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;url = f\"https://apitempo.inmet.gov.br/previsao/{station_code}\"<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;response = requests.get(url, timeout=10)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;data = response.json()<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;# Processa previsão de 5 dias<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;return format_weather_forecast(data)", code_style
    ))
    
    story.append(Paragraph("DuckDuckGo Search", heading2_style))
    story.append(Paragraph(
        "Motor de busca que preserva privacidade, usado para buscar informações atualizadas "
        "em fontes confiáveis de agricultura brasileira.", normal_style
    ))
    
    story.append(Paragraph("Fontes Confiáveis Configuradas:", heading3_style))
    story.append(Paragraph("• site:embrapa.br - Empresa Brasileira de Pesquisa Agropecuária", bullet_style))
    story.append(Paragraph("• site:epamig.br - Empresa de Pesquisa Agropecuária de Minas Gerais", bullet_style))
    story.append(Paragraph("• site:noticiasagricolas.com.br - Portal de notícias do agronegócio", bullet_style))
    story.append(Paragraph("• site:canalrural.com.br - Canal Rural", bullet_style))
    story.append(Paragraph("• site:globorural.globo.com - Globo Rural", bullet_style))
    story.append(Paragraph("• site:cepea.esalq.usp.br - Centro de Estudos Avançados em Economia Aplicada", bullet_style))
    
    story.append(PageBreak())
    
    # 7. Endpoints da API
    story.append(Paragraph("7. Endpoints da API", heading1_style))
    
    # Tabela de endpoints
    endpoints_data = [
        ["Método", "Endpoint", "Descrição", "Uso"],
        ["GET", "/unity/status", "Status da API e MongoDB", "Health check"],
        ["GET", "/unity/login/{unity_id}", "Login por Unity ID", "Autenticação"],
        ["POST", "/unity/profile/create", "Criar novo perfil", "Registro"],
        ["POST", "/unity/soil/save/{unity_id}", "Salvar dados de solo", "Simulação"],
        ["GET", "/unity/dashboard/{unity_id}", "Dashboard completo", "Interface"],
        ["GET", "/unity/monitoring/{unity_id}", "Monitoramento tempo real", "Gráficos"],
        ["GET", "/unity/analise-ia/{unity_id}", "Análise IA completa", "Diagnóstico"],
        ["POST", "/api/chat/{unity_id}", "Chat com streaming", "Chatbot"],
        ["POST", "/api/generate_title", "Gerar título conversa", "UI Chat"],
        ["POST", "/api/soil-tips/{unity_id}", "Dicas de melhoria", "Sugestões"]
    ]
    
    endpoints_table = Table(endpoints_data, colWidths=[0.6*inch, 1.8*inch, 1.4*inch, 0.8*inch])
    endpoints_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(endpoints_table)
    
    story.append(Paragraph("Exemplo de Resposta - Análise IA:", heading3_style))
    story.append(Paragraph(
        "{<br/>"
        "&nbsp;&nbsp;\"status\": \"success\",<br/>"
        "&nbsp;&nbsp;\"unity_id\": \"unity_bf87c29494e0\",<br/>"
        "&nbsp;&nbsp;\"diagnostico\": {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"saude_geral\": 78.5,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"alertas_criticos\": [<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"pH crítico: 5.2\",<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"Nitrogênio baixo: 15 mg/kg\"<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;],<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"parametros\": {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"ph\": {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"valor\": 5.2,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"status\": \"critico\",<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\"sugestao\": \"Aplicar calcário urgentemente\"<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;},<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;\"previsao_colheita\": \"Produtividade estimada: 520 toneladas\"<br/>"
        "&nbsp;&nbsp;}<br/>"
        "}", code_style
    ))
    
    story.append(PageBreak())
    
    # 8. Performance e Otimização
    story.append(Paragraph("8. Performance e Otimização", heading1_style))
    
    story.append(Paragraph("Estratégias de Performance", heading2_style))
    
    # Tabela de otimizações
    otimizacoes_data = [
        ["Técnica", "Implementação", "Benefício"],
        ["Async/Await", "FastAPI nativo", "I/O não bloqueante"],
        ["Streaming", "Server-Sent Events", "Respostas em tempo real"],
        ["Caching", "Embeddings pré-computados", "Busca RAG mais rápida"],
        ["Connection Pooling", "PyMongo com pool", "Reutilização de conexões"],
        ["Retry Logic", "Backoff exponencial", "Resiliência a falhas"],
        ["Indexação FAISS", "Vetores em memória", "Busca O(log n)"],
        ["Validação Pydantic", "Type hints Python", "Validação eficiente"]
    ]
    
    otimizacoes_table = Table(otimizacoes_data, colWidths=[1.2*inch, 1.8*inch, 1.5*inch])
    otimizacoes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(otimizacoes_table)
    
    story.append(Paragraph("Configuração de Retry com Backoff:", heading3_style))
    story.append(Paragraph(
        "retry_strategy = Retry(<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;total=3,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# 3 tentativas<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;backoff_factor=1,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Delay progressivo<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;status_forcelist=[429, 500, 502, 503, 504]&nbsp;&nbsp;# Códigos para retry<br/>"
        ")<br/><br/>"
        "# Timeouts configuráveis<br/>"
        "STREAM_TIMEOUT = 120&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Streaming do chatbot<br/>"
        "CONNECTION_TIMEOUT = 10&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Conexões HTTP<br/>"
        "NON_STREAM_TIMEOUT = 60&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Requisições normais", code_style
    ))
    
    story.append(PageBreak())
    
    # 9. Conclusão
    story.append(Paragraph("9. Conclusão", heading1_style))
    
    story.append(Paragraph("Pontos Fortes da Arquitetura", heading2_style))
    story.append(Paragraph("• <b>Modularidade:</b> Código bem organizado em módulos especializados", bullet_style))
    story.append(Paragraph("• <b>Escalabilidade:</b> MongoDB Atlas permite crescimento automático", bullet_style))
    story.append(Paragraph("• <b>Performance:</b> FastAPI + async/await para alta concorrência", bullet_style))
    story.append(Paragraph("• <b>IA Local:</b> Ollama elimina custos e garante privacidade", bullet_style))
    story.append(Paragraph("• <b>Robustez:</b> Tratamento de erros e retry automático", bullet_style))
    story.append(Paragraph("• <b>Documentação:</b> Swagger UI automático para todos os endpoints", bullet_style))
    
    story.append(Paragraph("Impacto e Inovação", heading2_style))
    story.append(Paragraph(
        "O projeto EKKO representa uma abordagem inovadora para a agricultura de precisão,"
        "combinando um dashboard que viabiliza o monitoramento em tempo real do solo e análises e recomendações ao agricultor"
        "embasadas em instituições renomadas de pesquisa agrícola. Demonstra maturidade no uso de ferramentas modernas como"
        "FastAPI, MongoDB Atlas e modelos de IA locais, resultando em uma solução robusta, escalável e"
        "economicamente viável para os pequenos agricultores do país.", normal_style
    ))
    
    story.append(Paragraph(
        "A integração do website com uma simulação 3D gamificada cria uma experiência de aprendizado, "
        "permitindo que o objetivo e funcionamento do projeto sejam facilmente compreendidos não só por agricultores "
        "e técnicos, mas também por qualquer um que esteja interessado, contribuindo para uma agricultura mais sustentável "
        "e produtiva no Brasil e para a democratização do conhecimento técnico. ", normal_style
    ))
    
    story.append(Spacer(1, 30))
    story.append(Paragraph("Equipe de Desenvolvimento", heading2_style))
    story.append(Paragraph("Turma: 34DS08", normal_style))
    story.append(Paragraph("Instituição: ETE FMC", normal_style))
    story.append(Paragraph("Evento: 45ª Projete", normal_style))
    story.append(Paragraph("Tema: Fraternidade e Ecologia Integral", normal_style))
    
    # Gerar PDF
    doc.build(story)
    print(f"PDF completo gerado com sucesso: {filename}")
    return filename

if __name__ == "__main__":
    criar_pdf_completo()