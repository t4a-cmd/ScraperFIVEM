@echo off
echo Lancement de dumpeer.py...
python dumpeer.py

if %errorlevel% neq 0 (
    echo Une erreur s'est produite lors de l'exécution de dumpeer.py.
    pause
    exit /b %errorlevel%
)

echo dumpeer.py s'est exécuté avec succès.
pause
