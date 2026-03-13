import sys

def main():
    print("--- TEST INFRASTRUTTURA PYTHON ---")
    print(f"Versione Interprete: {sys.version.split()[0]}")
    print(f"Eseguibile in uso: {sys.executable}")
    
    # Verifica logica dell'isolamento
    if ".venv" in sys.executable:
        print("[SUCCESS] Stai girando nell'ambiente virtuale isolato.")
    else:
        print("[FATAL ERROR] Stai usando l'interprete globale di sistema!")

if __name__ == "__main__":
    main()