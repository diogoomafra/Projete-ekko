#!/usr/bin/env python3
"""
Script para atualizar documentação automaticamente
"""

import subprocess
import sys
import os
from datetime import datetime

def gerar_documentacao():
    """Gera a documentação PDF atualizada"""
    try:
        print("🔄 Atualizando documentação...")
        
        # Executa o gerador de PDF
        result = subprocess.run([sys.executable, "gerar_pdf_completo.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Documentação atualizada com sucesso!")
            print(f"📄 Arquivo: EKKO_Backend_Tecnologias_Completo.pdf")
            print(f"📅 Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}")
        else:
            print("❌ Erro ao gerar documentação:")
            print(result.stderr)
            
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    gerar_documentacao()