#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de PDF - Frontend EKKO
Documentação completa das tecnologias do frontend
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.colors import HexColor, black, white, grey
from datetime import datetime

def criar_pdf_frontend():
    # Configuração do documento
    filename = "Frontend.pdf"
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
    story.append(Paragraph("Documentação Técnica do Frontend", doc_title_style))
    story.append(Paragraph("Interface Web, UX/UI e Funcionalidades", doc_subtitle_style))
    
    # Informações institucionais
    story.append(Spacer(1, 60))
    
    # Tabela de informações acadêmicas
    info_data = [
        ["", ""],
        ["Instituição:", "Escola Técnica de Eletrônica 'FMC'"],
        ["Curso:", "Desenvolvimento de Sistemas"],
        ["Equipe:", "34DS08"],
        ["Evento:", "45ª Projete - Fraternidade e Ecologia Integral"],
        ["Área:", "Interface Web e Experiência do Usuário"],
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
        "<i>\"A tecnologia é melhor quando aproxima as pessoas.\"</i>",
        dedicatoria_style
    ))
    
    story.append(Spacer(1, 40))
    
    story.append(Paragraph(
        "Dedicado aos desenvolvedores que,<br/>"
        "através do código e design,<br/>"
        "criam experiências que transformam vidas.",
        ParagraphStyle('DedicatoriaText', parent=dedicatoria_style, 
                      fontSize=11, textColor=HexColor('#52796F'))
    ))
    
    story.append(PageBreak())
    
    # Índice
    story.append(Paragraph("Índice", heading1_style))
    indice_data = [
        ["1.", "Visão Geral do Frontend", "3"],
        ["2.", "Tecnologias Web Fundamentais", "4"],
        ["3.", "Design e Interface (UI/UX)", "5"],
        ["4.", "JavaScript e Interatividade", "6"],
        ["5.", "Funcionalidades do Website", "7"],
        ["6.", "Dashboard Inteligente", "8"],
        ["7.", "Chatbot Integrado", "9"],
        ["8.", "Responsividade e Acessibilidade", "10"],
        ["9.", "Performance e Otimização", "11"],
        ["10.", "Estrutura de Arquivos", "12"]
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
    
    # 1. Visão Geral do Frontend
    story.append(Paragraph("1. Visão Geral do Frontend", heading1_style))
    
    story.append(Paragraph("Objetivo do Website", heading2_style))
    story.append(Paragraph(
        "O Ekko é uma plataforma web moderna que serve como interface principal "
        "para visualização e análise de dados e informações do solo a partir de tecnologias modernas. "
        "Desenvolvido com foco na experiência do usuário, oferece um dashboard inteligente "
        "com análises de IA, gráficos interativos e um chatbot especializado em agricultura.",
        normal_style
    ))
    
    story.append(Paragraph("Características Principais", heading2_style))
    
    # Tabela de características
    caracteristicas_data = [
        ["Aspecto", "Tecnologia", "Descrição"],
        ["Interface", "HTML5 + CSS3", "Design moderno com glassmorphism"],
        ["Interatividade", "JavaScript ES6+", "Funcionalidades dinâmicas"],
        ["Visualização", "Chart.js", "Gráficos e mapas de calor"],
        ["Comunicação", "Fetch API", "Integração com backend"],
        ["Responsividade", "CSS Grid/Flexbox", "Adaptável a todos dispositivos"],
        ["Acessibilidade", "ARIA + Semântica", "Inclusivo e acessível"]
    ]
    
    caracteristicas_table = Table(caracteristicas_data, colWidths=[1.5*inch, 2*inch, 2.5*inch])
    caracteristicas_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(caracteristicas_table)
    
    story.append(PageBreak())
    
    # 2. Tecnologias Web Fundamentais
    story.append(Paragraph("2. Tecnologias Web Fundamentais", heading1_style))
    
    story.append(Paragraph("HTML5 - Estrutura Semântica Moderna", heading2_style))
    story.append(Paragraph(
        "<b>HTML5</b> é a quinta versão da linguagem de marcação HTML, que fornece "
        "a estrutura semântica completa do website EKKO. Utilizamos elementos modernos "
        "para garantir melhor acessibilidade, SEO otimizado e compatibilidade com "
        "tecnologias assistivas. A estrutura semântica permite que motores de busca "
        "e leitores de tela compreendam melhor o conteúdo e sua hierarquia.", normal_style
    ))
    
    story.append(Paragraph("Elementos Semânticos Utilizados:", heading3_style))
    story.append(Paragraph("• <b>&lt;header&gt;:</b> Cabeçalho com navegação principal", bullet_style))
    story.append(Paragraph("• <b>&lt;nav&gt;:</b> Menus de navegação e breadcrumbs", bullet_style))
    story.append(Paragraph("• <b>&lt;main&gt;:</b> Conteúdo principal de cada página", bullet_style))
    story.append(Paragraph("• <b>&lt;section&gt;:</b> Seções temáticas do dashboard", bullet_style))
    story.append(Paragraph("• <b>&lt;article&gt;:</b> Conteúdo independente (cards, posts)", bullet_style))
    story.append(Paragraph("• <b>&lt;aside&gt;:</b> Sidebar do chat e informações auxiliares", bullet_style))
    story.append(Paragraph("• <b>&lt;footer&gt;:</b> Rodapé com informações da equipe", bullet_style))
    
    story.append(Paragraph("Estrutura Semântica:", heading3_style))
    story.append(Paragraph(
        "&lt;!DOCTYPE html&gt;<br/>"
        "&lt;html lang=\"pt-BR\"&gt;<br/>"
        "&lt;head&gt;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&lt;meta charset=\"UTF-8\"&gt;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"&gt;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&lt;title&gt;EKKO - Agricultura Inteligente&lt;/title&gt;<br/>"
        "&lt;/head&gt;<br/>"
        "&lt;body&gt;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&lt;header&gt;&lt;nav&gt;...&lt;/nav&gt;&lt;/header&gt;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&lt;main&gt;&lt;section&gt;...&lt;/section&gt;&lt;/main&gt;<br/>"
        "&lt;/body&gt;<br/>"
        "&lt;/html&gt;", code_style
    ))
    
    story.append(Paragraph("CSS3 - Design Moderno e Responsivo", heading2_style))
    story.append(Paragraph(
        "<b>CSS3</b> é responsável por toda a apresentação visual do EKKO, "
        "implementando um design moderno e sofisticado. Utilizamos técnicas avançadas "
        "como glassmorphism para criar efeitos de vidro translúcido, gradientes "
        "complexos para profundidade visual, animações CSS para transições suaves "
        "e um sistema de grid responsivo que se adapta a qualquer dispositivo. "
        "O código CSS é organizado em módulos especializados para facilitar "
        "manutenção e escalabilidade.", normal_style
    ))
    
    story.append(Paragraph("Técnicas CSS Avançadas Implementadas:", heading3_style))
    story.append(Paragraph("• <b>Glassmorphism:</b> backdrop-filter: blur(20px) para efeitos de vidro", bullet_style))
    story.append(Paragraph("• <b>CSS Grid:</b> Layout bidimensional para dashboards complexos", bullet_style))
    story.append(Paragraph("• <b>Flexbox:</b> Alinhamento e distribuição de elementos", bullet_style))
    story.append(Paragraph("• <b>Custom Properties:</b> Variáveis CSS para consistência de design", bullet_style))
    story.append(Paragraph("• <b>Animations:</b> @keyframes para transições e micro-interações", bullet_style))
    story.append(Paragraph("• <b>Media Queries:</b> Breakpoints para responsividade completa", bullet_style))
    
    story.append(Paragraph("Variáveis CSS Customizadas:", heading3_style))
    story.append(Paragraph(
        ":root {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--primary-green: #059669;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--secondary-green: #10B981;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--tech-blue: #3B82F6;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--purple: #8B5CF6;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--orange: #F59E0B;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--gray-50: #F9FAFB;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);<br/>"
        "}", code_style
    ))
    
    story.append(Paragraph("JavaScript ES6+ - Funcionalidades Avançadas", heading2_style))
    story.append(Paragraph(
        "<b>JavaScript ES6+</b> é o núcleo da interatividade do EKKO, utilizando "
        "recursos modernos da linguagem para criar uma experiência rica e responsiva. "
        "Implementamos programação assíncrona com async/await, módulos ES6 para "
        "organização do código, arrow functions para sintaxe concisa, destructuring "
        "para manipulação eficiente de dados, template literals para geração dinâmica "
        "de HTML, e classes ES6 para programação orientada a objetos. O código "
        "segue padrões modernos de desenvolvimento com tratamento robusto de erros.", normal_style
    ))
    
    story.append(Paragraph("Features ES6+ Utilizadas:", heading3_style))
    story.append(Paragraph("• <b>Async/Await:</b> Operações assíncronas elegantes", bullet_style))
    story.append(Paragraph("• <b>Arrow Functions:</b> Sintaxe concisa e escopo léxico", bullet_style))
    story.append(Paragraph("• <b>Template Literals:</b> Interpolação de strings e HTML", bullet_style))
    story.append(Paragraph("• <b>Destructuring:</b> Extração eficiente de propriedades", bullet_style))
    story.append(Paragraph("• <b>Spread Operator:</b> Manipulação de arrays e objetos", bullet_style))
    story.append(Paragraph("• <b>Modules:</b> Importação/exportação de funcionalidades", bullet_style))
    story.append(Paragraph("• <b>Classes:</b> Programação orientada a objetos moderna", bullet_style))
    
    story.append(PageBreak())
    
    # 3. Design e Interface (UI/UX)
    story.append(Paragraph("3. Design e Interface (UI/UX)", heading1_style))
    
    story.append(Paragraph("Filosofia de Design", heading2_style))
    story.append(Paragraph(
        "O design do EKKO segue princípios modernos de UX/UI com foco na "
        "usabilidade, acessibilidade e experiência visual agradável.", normal_style
    ))
    
    story.append(Paragraph("Elementos de Design:", heading3_style))
    story.append(Paragraph("• <b>Glassmorphism:</b> Efeitos de vidro translúcido com backdrop-filter", bullet_style))
    story.append(Paragraph("• <b>Gradientes:</b> Transições suaves de cores para profundidade", bullet_style))
    story.append(Paragraph("• <b>Sombras:</b> Sistema hierárquico de elevação", bullet_style))
    story.append(Paragraph("• <b>Tipografia:</b> Inter + Poppins para legibilidade", bullet_style))
    story.append(Paragraph("• <b>Ícones:</b> Font Awesome para consistência visual", bullet_style))
    
    story.append(Paragraph("Paleta de Cores", heading2_style))
    
    # Tabela de cores
    cores_data = [
        ["Cor", "Hex", "Uso"],
        ["Verde Primário", "#059669", "Elementos principais, CTAs"],
        ["Verde Secundário", "#10B981", "Destaques, sucesso"],
        ["Azul Tecnológico", "#3B82F6", "Links, informações"],
        ["Roxo", "#8B5CF6", "IA, análises avançadas"],
        ["Laranja", "#F59E0B", "Alertas, atenção"],
        ["Cinza 50", "#F9FAFB", "Backgrounds, cards"]
    ]
    
    cores_table = Table(cores_data, colWidths=[1.5*inch, 1*inch, 2.5*inch])
    cores_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(cores_table)
    
    story.append(Paragraph("Layout e Navegação", heading2_style))
    story.append(Paragraph(
        "Interface organizada em seções lógicas com navegação intuitiva e "
        "feedback visual imediato para todas as interações do usuário.", normal_style
    ))
    
    story.append(PageBreak())
    
    # 4. JavaScript e Interatividade
    story.append(Paragraph("4. JavaScript e Interatividade", heading1_style))
    
    story.append(Paragraph("Arquitetura JavaScript", heading2_style))
    story.append(Paragraph(
        "Código JavaScript modular e organizado em diferentes arquivos "
        "especializados para funcionalidades específicas.", normal_style
    ))
    
    story.append(Paragraph("Módulos Principais:", heading3_style))
    
    # Tabela de módulos JS
    modulos_data = [
        ["Arquivo", "Função", "Características"],
        ["unity-dashboard.js", "Dashboard principal", "Gestão de dados, navegação"],
        ["chat_bot.js", "Sistema de chat", "Streaming, sessões, histórico"],
        ["monitoring.js", "Monitoramento", "Gráficos tempo real"],
        ["correlation-engine.js", "Análise de dados", "Correlações, estatísticas"],
        ["index.js", "Homepage", "Animações, interações"]
    ]
    
    modulos_table = Table(modulos_data, colWidths=[1.3*inch, 1.5*inch, 2.2*inch])
    modulos_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#3B82F6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(modulos_table)
    
    story.append(Paragraph("Funcionalidades JavaScript:", heading3_style))
    story.append(Paragraph("• <b>Fetch API:</b> Comunicação assíncrona com backend", bullet_style))
    story.append(Paragraph("• <b>LocalStorage:</b> Persistência de dados do usuário", bullet_style))
    story.append(Paragraph("• <b>Event Listeners:</b> Interações responsivas", bullet_style))
    story.append(Paragraph("• <b>DOM Manipulation:</b> Atualizações dinâmicas", bullet_style))
    story.append(Paragraph("• <b>Error Handling:</b> Tratamento robusto de erros", bullet_style))
    
    story.append(Paragraph("Exemplo de Implementação:", heading3_style))
    story.append(Paragraph(
        "// Comunicação com API<br/>"
        "async loadUnityProfile(unityId) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;try {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;const response = await fetch(`${this.baseUrl}/unity/dashboard/${unityId}`);<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if (!response.ok) throw new Error(`HTTP ${response.status}`);<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;const data = await response.json();<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this.renderDashboard(data);<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;} catch (error) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;this.showError('Erro ao carregar dados');<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;}<br/>"
        "}", code_style
    ))
    
    story.append(PageBreak())
    
    # 5. Funcionalidades do Website
    story.append(Paragraph("5. Funcionalidades do Website", heading1_style))
    
    story.append(Paragraph("Homepage Interativa e Envolvente", heading2_style))
    story.append(Paragraph(
        "A homepage do EKKO foi projetada para causar impacto visual imediato e "
        "transmitir a missão do projeto de forma clara e envolvente. Utilizamos "
        "animações CSS e JavaScript para criar estatísticas que se animam conforme "
        "o usuário rola a página, efeitos de hover sofisticados em cards e botões, "
        "e transições suaves entre seções. A página é otimizada para conversão, "
        "guiando o usuário naturalmente do problema ambiental para a solução EKKO.", normal_style
    ))
    
    story.append(Paragraph("Seções Detalhadas da Homepage:", heading3_style))
    story.append(Paragraph("• <b>Hero Section:</b> Vídeo de fundo com overlay e CTA principal", bullet_style))
    story.append(Paragraph("• <b>Problema Ambiental:</b> Estatísticas alarmantes com animações", bullet_style))
    story.append(Paragraph("• <b>Solução EKKO:</b> Cards interativos explicando o projeto", bullet_style))
    story.append(Paragraph("• <b>Tecnologias:</b> Grid responsivo com ícones animados", bullet_style))
    story.append(Paragraph("• <b>Resultados:</b> Métricas de impacto com contadores animados", bullet_style))
    story.append(Paragraph("• <b>CTA Final:</b> Botão de ação com efeitos visuais", bullet_style))
    
    story.append(Paragraph("Elementos da Homepage:", heading3_style))
    story.append(Paragraph("• <b>Hero Section:</b> Apresentação visual impactante", bullet_style))
    story.append(Paragraph("• <b>Estatísticas Ambientais:</b> Dados animados sobre sustentabilidade", bullet_style))
    story.append(Paragraph("• <b>Sobre o Projeto:</b> Explicação detalhada do EKKO", bullet_style))
    story.append(Paragraph("• <b>Features:</b> Principais funcionalidades destacadas", bullet_style))
    story.append(Paragraph("• <b>Contato:</b> Informações da equipe e instituição", bullet_style))
    
    story.append(Paragraph("Sistema de Login", heading2_style))
    story.append(Paragraph(
        "Autenticação simples via ID único do usuário com validação e redirecionamento "
        "automático para o dashboard personalizado.", normal_style
    ))
    
    story.append(Paragraph("Dashboard Inteligente e Modular", heading2_style))
    story.append(Paragraph(
        "O dashboard do EKKO é uma interface sofisticada e modular que centraliza "
        "todas as funcionalidades do sistema em 8 seções especializadas. Cada seção "
        "foi projetada com foco na usabilidade e eficiência, utilizando lazy loading "
        "para otimizar performance, navegação intuitiva com feedback visual, "
        "atualizações em tempo real via WebSocket, e adaptação automática ao perfil "
        "do usuário. A interface segue princípios de Material Design e oferece "
        "acessibilidade completa via teclado e leitores de tela.", normal_style
    ))
    
    story.append(Paragraph("Arquitetura do Dashboard:", heading3_style))
    story.append(Paragraph("• <b>Sidebar Responsiva:</b> Navegação colapsável com ícones", bullet_style))
    story.append(Paragraph("• <b>Conteúdo Dinâmico:</b> Carregamento assíncrono de seções", bullet_style))
    story.append(Paragraph("• <b>Estado Global:</b> Gerenciamento centralizado de dados", bullet_style))
    story.append(Paragraph("• <b>Cache Inteligente:</b> Persistência local para performance", bullet_style))
    story.append(Paragraph("• <b>Error Handling:</b> Tratamento gracioso de falhas", bullet_style))
    story.append(Paragraph("• <b>Loading States:</b> Indicadores visuais de carregamento", bullet_style))
    
    story.append(PageBreak())
    
    # Tabela de seções do dashboard
    story.append(Paragraph("Seções do Dashboard:", heading3_style))
    secoes_data = [
        ["Seção", "Funcionalidade"],
        ["Dashboard", "Visão geral e métricas principais"],
        ["Perfil", "Dados pessoais e propriedade"],
        ["IA & Solo", "Análise inteligente de 12 parâmetros"],
        ["Relatórios", "Gráficos e mapas de calor"],
        ["Simulação", "Histórico de sessões da simulação"],
        ["Sistema", "Documentação técnica"],
        ["Monitoramento", "Dados em tempo real"],
        ["Chatbot", "Assistente IA especializado em agricultura"]
    ]
    
    secoes_table = Table(secoes_data, colWidths=[1.5*inch, 3.5*inch])
    secoes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#8B5CF6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(secoes_table)
    
    # 6. Dashboard Inteligente
    story.append(Paragraph("6. Dashboard Inteligente", heading1_style))
    
    story.append(Paragraph("Sistema Avançado de Visualização de Dados", heading2_style))
    story.append(Paragraph(
        "O sistema de visualização do EKKO transforma dados complexos de solo em "
        "insights visuais compreensíveis e acionáveis. Utilizamos Chart.js como base, "
        "mas implementamos customizações avançadas incluindo paletas de cores "
        "temáticas, animações personalizadas, tooltips informativos, zoom e pan "
        "interativo, exportação de gráficos, e sincronização entre múltiplas "
        "visualizações. Os gráficos são totalmente responsivos e acessíveis.", normal_style
    ))
    
    story.append(Paragraph("Recursos Avançados de Visualização:", heading3_style))
    story.append(Paragraph("• <b>Mapas de Calor Interativos:</b> Visualização espacial de parâmetros", bullet_style))
    story.append(Paragraph("• <b>Gráficos Temporais:</b> Evolução histórica com zoom", bullet_style))
    story.append(Paragraph("• <b>Dashboards Personalizados:</b> Widgets drag-and-drop", bullet_style))
    story.append(Paragraph("• <b>Alertas Visuais:</b> Indicações de status crítico", bullet_style))
    story.append(Paragraph("• <b>Comparações:</b> Análise lado a lado de períodos", bullet_style))
    story.append(Paragraph("• <b>Exportação:</b> PNG, SVG, PDF para relatórios", bullet_style))
    
    story.append(Paragraph("Chart.js Integration", heading2_style))
    story.append(Paragraph(
        "Biblioteca JavaScript para criação de gráficos responsivos "
        "e interativos com diferentes tipos de visualização.", normal_style
    ))
    
    story.append(Paragraph("Tipos de Gráficos Implementados:", heading3_style))
    story.append(Paragraph("• <b>Line Charts:</b> Evolução temporal dos parâmetros", bullet_style))
    story.append(Paragraph("• <b>Bar Charts:</b> Comparação entre diferentes valores", bullet_style))
    story.append(Paragraph("• <b>Heatmaps:</b> Mapas de calor para análise espacial", bullet_style))
    story.append(Paragraph("• <b>Radar Charts:</b> Análise multidimensional", bullet_style))
    
    story.append(Paragraph("Exemplo de Configuração Chart.js:", heading3_style))
    story.append(Paragraph(
        "const chartConfig = {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;type: 'line',<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;data: {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;labels: ['Jan', 'Fev', 'Mar'],<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;datasets: [{<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label: 'pH do Solo',<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data: [6.2, 6.5, 6.8],<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;borderColor: '#10B981',<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tension: 0.4<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}]<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;},<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;options: {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;responsive: true,<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maintainAspectRatio: false<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;}<br/>"
        "};", code_style
    ))
    
    story.append(Paragraph("Análise de IA Integrada", heading2_style))
    story.append(Paragraph(
        "Interface para visualização das análises de inteligência artificial "
        "com recomendações personalizadas e alertas críticos.", normal_style
    ))
    
    story.append(PageBreak())
    
    # 7. Chatbot Integrado
    story.append(Paragraph("7. Chatbot Integrado", heading1_style))
    
    story.append(Paragraph("Sistema de Chat com IA Avançada", heading2_style))
    story.append(Paragraph(
        "O sistema de chat do EKKO representa o estado da arte em interfaces "
        "conversacionais para agricultura. Integrado com IA Llama 3.2 via Ollama, "
        "oferece respostas especializadas em tempo real com streaming de texto, "
        "contextualização automática baseada no perfil do usuário, acesso a dados "
        "climáticos via geolocalização, busca em base de conhecimento agrícola, "
        "e geração automática de títulos para conversas. A interface é intuitiva "
        "com sidebar retrátil, suporte a markdown, e persistência local de histórico.", normal_style
    ))
    
    story.append(Paragraph("Funcionalidades Técnicas do Chat:", heading3_style))
    story.append(Paragraph("• <b>Server-Sent Events:</b> Streaming de respostas em tempo real", bullet_style))
    story.append(Paragraph("• <b>Context Management:</b> Manutenção de contexto entre mensagens", bullet_style))
    story.append(Paragraph("• <b>Session Isolation:</b> Conversas isoladas por usuário", bullet_style))
    story.append(Paragraph("• <b>Geolocation API:</b> Previsões climáticas precisas", bullet_style))
    story.append(Paragraph("• <b>RAG Integration:</b> Busca em base de conhecimento", bullet_style))
    story.append(Paragraph("• <b>Auto-titling:</b> IA gera títulos para conversas", bullet_style))
    story.append(Paragraph("• <b>Error Recovery:</b> Reconexão automática em falhas", bullet_style))
    
    story.append(Paragraph("Funcionalidades do Chat:", heading3_style))
    story.append(Paragraph("• <b>Streaming:</b> Respostas em tempo real via Server-Sent Events", bullet_style))
    story.append(Paragraph("• <b>Sessões:</b> Múltiplas conversas organizadas", bullet_style))
    story.append(Paragraph("• <b>Histórico:</b> Persistência local das conversas", bullet_style))
    story.append(Paragraph("• <b>Geolocalização:</b> Previsões climáticas precisas", bullet_style))
    story.append(Paragraph("• <b>Títulos IA:</b> Geração automática de títulos", bullet_style))
    
    story.append(Paragraph("Implementação do Streaming:", heading3_style))
    story.append(Paragraph(
        "// Streaming de respostas do chatbot<br/>"
        "const response = await fetch(API_URL_CHAT, {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;method: 'POST',<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;headers: { 'Content-Type': 'application/json' },<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;body: JSON.stringify({ message: question, history: chatHistory })<br/>"
        "});<br/><br/>"
        "const reader = response.body.getReader();<br/>"
        "const decoder = new TextDecoder();<br/><br/>"
        "while (true) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;const { value, done } = await reader.read();<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;if (done) break;<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;const chunk = decoder.decode(value, { stream: true });<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;updateBotMessage(chunk);<br/>"
        "}", code_style
    ))
    
    story.append(Paragraph("Interface do Chat", heading2_style))
    story.append(Paragraph(
        "Design moderno com sidebar retrátil, botões de ação e "
        "indicadores visuais de status da conversa.", normal_style
    ))
    
    story.append(PageBreak())
    
    # 8. Responsividade e Acessibilidade
    story.append(Paragraph("8. Responsividade e Acessibilidade", heading1_style))
    
    story.append(Paragraph("Design Responsivo", heading2_style))
    story.append(Paragraph(
        "Layout adaptável que funciona perfeitamente em desktop, "
        "tablet e dispositivos móveis usando CSS Grid e Flexbox.", normal_style
    ))
    
    story.append(Paragraph("Breakpoints Principais:", heading3_style))
    story.append(Paragraph(
        "@media (max-width: 768px) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;.sidebar { transform: translateX(-100%); }<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;.main-content { margin-left: 0; }<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;.container { padding: 1rem; }<br/>"
        "}<br/><br/>"
        "@media (max-width: 1200px) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;.unity-info-grid { grid-template-columns: 1fr 1fr; }<br/>"
        "}<br/><br/>"
        "@media (max-width: 900px) {<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;.unity-info-grid { grid-template-columns: 1fr; }<br/>"
        "}", code_style
    ))
    
    story.append(Paragraph("Acessibilidade", heading2_style))
    story.append(Paragraph(
        "Implementação de práticas de acessibilidade para garantir "
        "que o website seja utilizável por todos os usuários.", normal_style
    ))
    
    story.append(Paragraph("Recursos de Acessibilidade:", heading3_style))
    story.append(Paragraph("• <b>Semântica HTML:</b> Elementos estruturais apropriados", bullet_style))
    story.append(Paragraph("• <b>ARIA Labels:</b> Descrições para leitores de tela", bullet_style))
    story.append(Paragraph("• <b>Contraste:</b> Cores com contraste adequado (WCAG)", bullet_style))
    story.append(Paragraph("• <b>Navegação:</b> Suporte completo ao teclado", bullet_style))
    story.append(Paragraph("• <b>Alt Text:</b> Descrições para todas as imagens", bullet_style))
    
    story.append(PageBreak())
    
    # 9. Performance e Otimização
    story.append(Paragraph("9. Performance e Otimização", heading1_style))
    
    story.append(Paragraph("Otimizações Implementadas", heading2_style))
    
    # Tabela de otimizações
    otimizacoes_data = [
        ["Técnica", "Implementação", "Benefício"],
        ["Lazy Loading", "Carregamento sob demanda", "Reduz tempo inicial"],
        ["Minificação", "CSS/JS comprimidos", "Menor tamanho de arquivos"],
        ["Caching", "LocalStorage + SessionStorage", "Dados persistentes"],
        ["Async/Await", "Operações não bloqueantes", "Interface responsiva"],
        ["Debouncing", "Controle de eventos", "Melhor performance"],
        ["Image Optimization", "Formatos otimizados", "Carregamento rápido"]
    ]
    
    otimizacoes_table = Table(otimizacoes_data, colWidths=[1.5*inch, 2.2*inch, 1.8*inch])
    otimizacoes_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#F59E0B')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(otimizacoes_table)
    
    story.append(Paragraph("Métricas de Performance", heading2_style))
    story.append(Paragraph(
        "Website otimizado para carregamento rápido e experiência "
        "fluida do usuário em diferentes condições de rede.", normal_style
    ))
    
    story.append(PageBreak())
    
    # 10. Estrutura de Arquivos
    story.append(Paragraph("10. Estrutura de Arquivos", heading1_style))
    
    story.append(Paragraph("Organização do Projeto", heading2_style))
    story.append(Paragraph(
        "Frontend//<br/>"
        "├── pages//<br/>"
        "│&nbsp;&nbsp;&nbsp;├── index.html&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Homepage<br/>"
        "│&nbsp;&nbsp;&nbsp;├── login.html&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Login por Unity ID<br/>"
        "│&nbsp;&nbsp;&nbsp;└── dashboard.html&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Dashboard principal<br/>"
        "├── css//<br/>"
        "│&nbsp;&nbsp;&nbsp;├── index.css&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Estilos homepage<br/>"
        "│&nbsp;&nbsp;&nbsp;├── login.css&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Estilos login<br/>"
        "│&nbsp;&nbsp;&nbsp;├── dashboard.css&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Estilos dashboard<br/>"
        "│&nbsp;&nbsp;&nbsp;├── chat_bot.css&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Estilos chatbot<br/>"
        "│&nbsp;&nbsp;&nbsp;├── monitoring.css&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Estilos monitoramento<br/>"
        "│&nbsp;&nbsp;&nbsp;└── modal.css&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Estilos modais<br/>"
        "├── js//<br/>"
        "│&nbsp;&nbsp;&nbsp;├── index.js&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Lógica homepage<br/>"
        "│&nbsp;&nbsp;&nbsp;├── unity-dashboard.js&nbsp;&nbsp;&nbsp;&nbsp;# JavaScript dashboard<br/>"
        "│&nbsp;&nbsp;&nbsp;├── chat_bot.js&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Sistema de chat<br/>"
        "│&nbsp;&nbsp;&nbsp;├── monitoring.js&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Monitoramento<br/>"
        "│&nbsp;&nbsp;&nbsp;└── correlation-engine.js&nbsp;# Análise de dados<br/>"
        "└── assets//<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;└── images//<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── Fundo_menu.png<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├── inicio.jpg<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└── welcome-illustration.svg", code_style
    ))
    
    story.append(Paragraph("Dependências Externas", heading2_style))
    
    # Tabela de dependências
    dependencias_data = [
        ["Biblioteca", "Versão", "Uso"],
        ["Font Awesome", "6.0.0", "Ícones vetoriais"],
        ["Google Fonts", "Latest", "Tipografia (Inter + Poppins)"],
        ["Chart.js", "Latest", "Gráficos interativos"],
        ["Fetch API", "Nativo", "Comunicação HTTP"],
        ["LocalStorage", "Nativo", "Persistência de dados"]
    ]
    
    dependencias_table = Table(dependencias_data, colWidths=[1.5*inch, 1*inch, 2.5*inch])
    dependencias_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#2E8B57')),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('GRID', (0, 0), (-1, -1), 1, black)
    ]))
    story.append(dependencias_table)
    
    # Conclusão
    story.append(Spacer(1, 20))
    story.append(Paragraph("Conclusão", heading1_style))
    story.append(Paragraph(
        "O frontend do EKKO representa uma implementação moderna e completa de "
        "tecnologias web, combinando design atrativo, funcionalidades avançadas "
        "e experiência do usuário otimizada. A arquitetura modular e as práticas "
        "de desenvolvimento seguem padrões da indústria, resultando em uma "
        "plataforma robusta e escalável para agricultura inteligente.",
        normal_style
    ))
    
    # Gerar PDF
    doc.build(story)
    print(f"PDF do frontend gerado com sucesso: {filename}")
    return filename

if __name__ == "__main__":
    criar_pdf_frontend()