import subprocess
import sys

required_modules = [
    "requests",
    "fake_useragent",
    "colorama",
    "fade",
    "uuid",
    "py-socket"
]
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
input("Appuyez sur 'Entrée' pour commencer l'installation des modules nécessaires...")
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Le module {module} n'est pas installé. Installation en cours...")
        install(module)
print("Tous les modules sont installés avec succès.")
input("Tout est terminé. Appuyez sur 'Entrée' pour quitter.")