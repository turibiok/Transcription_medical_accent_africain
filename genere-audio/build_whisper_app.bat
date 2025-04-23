@echo off
echo [BUILD] Création de l'exécutable...
pyinstaller --onefile whisper_to_bark_local.spec
pause