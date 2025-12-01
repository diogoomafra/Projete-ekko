@echo off
echo ========================================
echo CORREÇÃO RÁPIDA - PROBLEMAS OLLAMA
echo ========================================

echo.
echo 1. Verificando se Ollama está rodando...
tasklist /FI "IMAGENAME eq ollama.exe" 2>NUL | find /I /N "ollama.exe">NUL
if "%ERRORLEVEL%"=="0" (
    echo ✅ Ollama está rodando
) else (
    echo ❌ Ollama não está rodando
    echo 🔧 Iniciando Ollama...
    start /B ollama serve
    timeout /t 5 /nobreak >nul
)

echo.
echo 2. Verificando modelo llama3.2...
ollama list | find "llama3.2" >nul
if %errorlevel%==0 (
    echo ✅ Modelo llama3.2 encontrado
) else (
    echo ❌ Modelo llama3.2 não encontrado
    echo 🔧 Baixando modelo llama3.2...
    ollama pull llama3.2
)

echo.
echo 3. Testando conexão...
python diagnose_ollama.py

echo.
echo 4. Reiniciando servidor se necessário...
echo 🔧 Parando processos Python...
taskkill /F /IM python.exe 2>nul

echo 🔧 Aguardando 3 segundos...
timeout /t 3 /nobreak >nul

echo 🔧 Iniciando servidor...
start /B python main.py

echo.
echo ========================================
echo CORREÇÃO CONCLUÍDA
echo ========================================
echo.
echo Se ainda houver problemas:
echo 1. Reinicie o computador
echo 2. Execute: ollama serve
echo 3. Execute: python main.py
echo.
pause