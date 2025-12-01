# Configurações do Ollama
OLLAMA_HOST = "localhost"
OLLAMA_PORT = 11434
OLLAMA_MODEL = "llama3.2:latest"

# Timeouts (em segundos)
CONNECTION_TIMEOUT = 10
STREAM_TIMEOUT = 120
NON_STREAM_TIMEOUT = 60

# Retry settings
MAX_RETRIES = 3
RETRY_BACKOFF_FACTOR = 1
RETRY_DELAY_BASE = 2

# Parâmetros do modelo
MODEL_OPTIONS = {
    "num_predict": 500,
    "temperature": 0.7,
    "top_p": 0.9
}

# URLs
OLLAMA_BASE_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}"
OLLAMA_API_URL = f"{OLLAMA_BASE_URL}/api/generate"
OLLAMA_CHAT_URL = f"{OLLAMA_BASE_URL}/api/chat"
OLLAMA_TAGS_URL = f"{OLLAMA_BASE_URL}/api/tags"