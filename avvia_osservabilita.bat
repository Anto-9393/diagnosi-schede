@echo off
REM Avvia losservabilita del progetto: exporter metriche + Prometheus + Grafana (stack "ops" di S11).
REM Uso: doppio clic su questo file (Docker Desktop deve essere acceso: "Engine running").
cd /d "%~dp0"
echo [1/4] Controllo Docker...
docker info >nul 2>&1 || (echo Docker non risponde: apri Docker Desktop e aspetta "Engine running", poi riprova. & pause & exit /b 1)
echo [2/4] Pacchetti Python (prometheus_client)...
call .venv\Scripts\python.exe -m pip install -q -r requirements.txt
echo [3/4] Avvio exporter metriche in una nuova finestra (porta 8001)...
start "Metriche diagnosi (non chiudere)" cmd /k ".venv\Scripts\python.exe -m diagnosi.metriche"
timeout /t 3 >nul
echo [4/4] Avvio Prometheus e Grafana...
cd observability
docker compose up -d
if errorlevel 1 (echo Errore di docker compose: copia questo messaggio. & pause & exit /b 1)
timeout /t 8 >nul
start "" http://localhost:9090/targets
start "" "http://localhost:3000/d/diagnosi-schede"
echo.
echo Fatto. Grafana: http://localhost:3000  -  Prometheus: http://localhost:9090/targets
echo Per fermare: in questa cartella "cd observability" e "docker compose down", e chiudi la finestra delle metriche.
pause
