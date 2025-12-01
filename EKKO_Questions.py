#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EKKO Project Questions Generator
Generates a PDF with questions about the EKKO agricultural precision project
organized by difficulty levels (Easy, Medium, Hard)
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.colors import HexColor
from datetime import datetime

def create_ekko_questions_pdf():
    """Creates PDF with EKKO project questions organized by difficulty levels"""
    
    # PDF setup
    filename = "EKKO_Project_Questions.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4, topMargin=0.8*inch, bottomMargin=0.8*inch)
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Title'],
        fontSize=24,
        textColor=HexColor("#4CAF50"),
        spaceAfter=30,
        alignment=1  # Center
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor("#000000"),
        spaceAfter=20,
        spaceBefore=20,
        alignment=1  # Center
    )
    
    level_style = ParagraphStyle(
        'LevelStyle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=HexColor('#4CAF50'),
        spaceAfter=15,
        spaceBefore=25
    )
    
    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=12,
        leftIndent=20
    )
    
    # Content
    content = []
    
    # Title
    content.append(Paragraph("EKKO", title_style))
    content.append(Paragraph("Questions for Analysis and Discussion", subtitle_style))
    content.append(Spacer(1, 20))
    
    # Project overview
    overview = """
    <b>Project Overview:</b><br/>
    Ekko is an integrated system that combines a web platform with a 3D simulation developed in Unity
    to teach and promote sustainable agriculture through intelligent analysis. The system includes AI-powered 
    soil analysis, real-time monitoring, specialized chatbot, and modern dashboard visualization.
    """
    content.append(Paragraph(overview, styles['Normal']))
    content.append(Spacer(1, 30))
    
    # EASY LEVEL QUESTIONS
    content.append(Paragraph("EASY LEVEL QUESTIONS", level_style))
    
    easy_questions = [
        "What is the main purpose of the EKKO project?",
        "Which technologies are used in the backend development?",
        "What type of simulation does EKKO provide to users?",
        "How many soil parameters does the AI system analyze?",
        "What is the primary programming language used for the backend API?",
        "Which database system is used to store user and soil data?",
        "What is the main benefit of using Unity 3D in this project?",
        "How does the system help farmers learn about sustainable agriculture?",
        "What type of chatbot technology is integrated into the system?",
        "Which web technologies are used for the frontend interface?",
        "What is the purpose of the dashboard in the EKKO system?",
        "How does the system monitor crops in real-time?",
        "What is the significance of the RAG (Retrieval-Augmented Generation) system?",
        "Which API is used for weather data integration?",
        "What is the main target audience for this agricultural system?"
    ]
    
    for i, question in enumerate(easy_questions, 1):
        content.append(Paragraph(f"{i}. {question}", question_style))
    
    content.append(PageBreak())
    
    # MEDIUM LEVEL QUESTIONS
    content.append(Paragraph("MEDIUM LEVEL QUESTIONS", level_style))
    
    medium_questions = [
        "Explain how the AI analyzer evaluates soil health using the 9 different parameters.",
        "Describe the integration between Unity 3D simulation and the web-based dashboard.",
        "How does the streaming chat system work with Llama 3.2 model?",
        "What are the advantages of using MongoDB Atlas for this agricultural application?",
        "Analyze the role of FastAPI in creating a scalable backend architecture.",
        "How does the system implement user session isolation for different Unity IDs?",
        "Explain the importance of the INMET weather API integration for farmers.",
        "Describe how the RAG system enhances the chatbot's agricultural knowledge.",
        "What is the significance of the sustainability calculation in soil analysis?",
        "How does the system handle real-time data processing and visualization?",
        "Explain the correlation between soil parameters and crop productivity predictions.",
        "Describe the security measures implemented in the API endpoints.",
        "How does the system provide personalized recommendations based on user profiles?",
        "What are the benefits of using Chart.js for data visualization in agriculture?",
        "Analyze the scalability potential of the EKKO architecture for large-scale deployment."
    ]
    
    for i, question in enumerate(medium_questions, 1):
        content.append(Paragraph(f"{i}. {question}", question_style))
    
    content.append(PageBreak())
    
    # HARD LEVEL QUESTIONS
    content.append(Paragraph("HARD LEVEL QUESTIONS", level_style))
    
    hard_questions = [
        "Critically evaluate the AI-driven soil analysis system's accuracy and potential limitations in real-world agricultural scenarios.",
        "Design an improvement strategy for the current chatbot system to handle complex agricultural decision-making processes.",
        "Analyze the economic impact and cost-benefit analysis of implementing EKKO in small to medium-sized farms.",
        "Propose a machine learning enhancement that could predict crop diseases based on the current soil parameter monitoring system.",
        "Evaluate the environmental sustainability implications of the EKKO system and its potential contribution to precision agriculture.",
        "Design a scalable architecture modification to support thousands of concurrent users while maintaining real-time performance.",
        "Critically assess the integration challenges between Unity 3D simulation and web technologies, proposing solutions for optimization.",
        "Develop a comprehensive data privacy and security framework for handling sensitive agricultural and personal data.",
        "Analyze the potential for integrating IoT sensors with the current EKKO system for automated data collection.",
        "Propose a methodology for validating the AI recommendations against actual crop yield outcomes.",
        "Design an extension of the system to support multiple crop types and regional agricultural variations.",
        "Evaluate the system's potential for integration with existing farm management software and government agricultural databases.",
        "Critically analyze the user experience design and propose improvements for farmer adoption and engagement.",
        "Develop a business model for commercializing the EKKO system while ensuring accessibility for small-scale farmers.",
        "Propose advanced analytics features that could provide predictive insights for long-term agricultural planning."
    ]
    
    for i, question in enumerate(hard_questions, 1):
        content.append(Paragraph(f"{i}. {question}", question_style))
    
    content.append(Spacer(1, 30))
    
    # Footer information
    footer_info = f"""
    <b>Document Information:</b><br/>
    Generated on: {datetime.now().strftime('%B %d, %Y')}<br/>
    Project: EKKO - Precision Agriculture System<br/>
    Team: 34DS08 | Institution: ETE FMC<br/>
    Location: Santa Rita do Sapucaí, MG, Brazil<br/>
    Total Questions: {len(easy_questions) + len(medium_questions) + len(hard_questions)}
    """
    content.append(Paragraph(footer_info, styles['Normal']))
    
    # Build PDF
    doc.build(content)
    print(f"PDF created successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_ekko_questions_pdf()