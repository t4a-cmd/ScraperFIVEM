@echo off
echo Installation des modules Python...
python install_modules.py

if %errorlevel% neq 0 (
    echo Une erreur s'est produite lors de l'installation des modules.
    pause
    exit /b %errorlevel%
)

echo Modules installés avec succès.
pause
