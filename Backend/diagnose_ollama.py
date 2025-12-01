#!/usr/bin/env python3
"""
Script de diagnóstico do Ollama
Verifica conexão, modelos disponíveis e performance
"""

import requests
import time
import json
from ollama_config import *

def check_ollama_service():
    """Verifica se o serviço Ollama está rodando"""
    print("Verificando servico Ollama...")
    try:
        response = requests.get(OLLAMA_TAGS_URL, timeout=CONNECTION_TIMEOUT)
        if response.status_code == 200:
            print("OK - Ollama esta rodando")
            return True
        else:
            print(f"ERRO - Ollama retornou status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("ERRO - Nao foi possivel conectar ao Ollama")
        print("   Certifique-se de que o Ollama está rodando: ollama serve")
        return False
    except Exception as e:
        print(f"ERRO - Erro ao verificar Ollama: {e}")
        return False

def check_model_availability():
    """Verifica se o modelo está disponível"""
    print(f"\nVerificando modelo {OLLAMA_MODEL}...")
    try:
        response = requests.get(OLLAMA_TAGS_URL, timeout=CONNECTION_TIMEOUT)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [model['name'] for model in models]
            
            if OLLAMA_MODEL in model_names:
                print(f"OK - Modelo {OLLAMA_MODEL} esta disponivel")
                return True
            else:
                print(f"ERRO - Modelo {OLLAMA_MODEL} nao encontrado")
                print("   Modelos disponíveis:", model_names)
                print(f"   Execute: ollama pull {OLLAMA_MODEL}")
                return False
        else:
            print(f"ERRO - Erro ao listar modelos: {response.status_code}")
            return False
    except Exception as e:
        print(f"ERRO - Erro ao verificar modelo: {e}")
        return False

def test_simple_request():
    """Testa uma requisição simples"""
    print(f"\nTestando requisicao simples...")
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "user", "content": "Responda apenas 'OK'"}
            ],
            "stream": False,
            "options": {
                "num_predict": 10,
                "temperature": 0.1
            }
        }
        
        start_time = time.time()
        response = requests.post(OLLAMA_CHAT_URL, json=payload, timeout=30)
        end_time = time.time()
        
        if response.status_code == 200:
            data = response.json()
            content = data.get('message', {}).get('content', '')
            duration = end_time - start_time
            print(f"OK - Requisicao bem-sucedida em {duration:.2f}s")
            print(f"   Resposta: {content.strip()}")
            return True
        else:
            print(f"ERRO - Requisicao falhou: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return False
            
    except requests.exceptions.ReadTimeout:
        print("ERRO - Timeout na requisicao (30s)")
        return False
    except Exception as e:
        print(f"ERRO - Erro na requisicao: {e}")
        return False

def test_streaming_request():
    """Testa uma requisição com streaming"""
    print(f"\nTestando requisicao com streaming...")
    try:
        payload = {
            "model": OLLAMA_MODEL,
            "messages": [
                {"role": "user", "content": "Conte até 3"}
            ],
            "stream": True,
            "options": {
                "num_predict": 20,
                "temperature": 0.1
            }
        }
        
        start_time = time.time()
        response = requests.post(OLLAMA_CHAT_URL, json=payload, stream=True, timeout=60)
        
        if response.status_code == 200:
            chunks_received = 0
            full_response = ""
            
            for chunk in response.iter_lines():
                if chunk:
                    try:
                        json_chunk = json.loads(chunk)
                        message = json_chunk.get("message", {}).get("content", "")
                        if message:
                            full_response += message
                            chunks_received += 1
                    except json.JSONDecodeError:
                        continue
            
            end_time = time.time()
            duration = end_time - start_time
            print(f"OK - Streaming bem-sucedido em {duration:.2f}s")
            print(f"   Chunks recebidos: {chunks_received}")
            print(f"   Resposta: {full_response.strip()}")
            return True
        else:
            print(f"ERRO - Streaming falhou: {response.status_code}")
            return False
            
    except requests.exceptions.ReadTimeout:
        print("ERRO - Timeout no streaming (60s)")
        return False
    except Exception as e:
        print(f"ERRO - Erro no streaming: {e}")
        return False

def show_configuration():
    """Mostra a configuração atual"""
    print("\nConfiguracao atual:")
    print(f"   Host: {OLLAMA_HOST}:{OLLAMA_PORT}")
    print(f"   Modelo: {OLLAMA_MODEL}")
    print(f"   Timeout conexão: {CONNECTION_TIMEOUT}s")
    print(f"   Timeout streaming: {STREAM_TIMEOUT}s")
    print(f"   Timeout não-streaming: {NON_STREAM_TIMEOUT}s")
    print(f"   Max retries: {MAX_RETRIES}")

def main():
    print("DIAGNOSTICO DO OLLAMA")
    print("=" * 50)
    
    show_configuration()
    
    # Verificações sequenciais
    checks = [
        ("Serviço Ollama", check_ollama_service),
        ("Modelo disponível", check_model_availability),
        ("Requisição simples", test_simple_request),
        ("Requisição streaming", test_streaming_request)
    ]
    
    results = []
    for name, check_func in checks:
        result = check_func()
        results.append((name, result))
        if not result:
            print(f"\nFalha em: {name}")
            break
    
    print("\n" + "=" * 50)
    print("RESUMO DOS TESTES:")
    for name, result in results:
        status = "PASSOU" if result else "FALHOU"
        print(f"   {name}: {status}")
    
    all_passed = all(result for _, result in results)
    if all_passed:
        print("\nTodos os testes passaram! Ollama esta funcionando corretamente.")
    else:
        print("\nAlguns testes falharam. Verifique as mensagens acima.")

if __name__ == "__main__":
    main()