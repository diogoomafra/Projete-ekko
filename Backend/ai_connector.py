import requests
import json
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from ollama_config import *

def create_session_with_retries():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session

def test_ollama_connection():
    try:
        session = create_session_with_retries()
        response = session.get(OLLAMA_TAGS_URL, timeout=CONNECTION_TIMEOUT)
        return response.status_code == 200
    except:
        return False

def get_ollama_response(prompt: str, stream: bool = False):
    if not test_ollama_connection():
        raise Exception("Ollama não está rodando! Execute: ollama serve")
    
    print(f"--- CONECTOR IA: Enviando para llama3.2 (Stream: {stream}) ---")
    
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": "Você é Ekko, assistente de agricultura."},
            {"role": "user", "content": prompt}
        ],
        "stream": stream,
        "options": MODEL_OPTIONS
    }
    
    max_retries = MAX_RETRIES
    base_timeout = STREAM_TIMEOUT if stream else NON_STREAM_TIMEOUT
    
    for attempt in range(max_retries):
        try:
            print(f"Tentativa {attempt + 1}/{max_retries} - Timeout: {base_timeout}s")
            
            session = create_session_with_retries()
            response = session.post(
                OLLAMA_CHAT_URL, 
                json=payload, 
                stream=stream, 
                timeout=base_timeout
            )
            response.raise_for_status()
            return response
            
        except requests.exceptions.ReadTimeout as e:
            print(f"Timeout na tentativa {attempt + 1}: {e}")
            if attempt < max_retries - 1:
                wait_time = RETRY_DELAY_BASE ** attempt
                print(f"Aguardando {wait_time}s antes da próxima tentativa...")
                time.sleep(wait_time)
                base_timeout += 30  # Aumenta timeout a cada tentativa
            else:
                print("ERRO: Todas as tentativas falharam por timeout")
                raise Exception(f"Ollama timeout após {max_retries} tentativas")
                
        except Exception as e:
            print(f"ERRO Ollama (tentativa {attempt + 1}): {e}")
            if attempt < max_retries - 1:
                time.sleep(1)
            else:
                raise