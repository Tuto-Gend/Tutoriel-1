import os
import base64

password_file = "config/password.txt"
data_file = "config/data.txt"
expected_password = base64.b64decode("cGFzc3dvcmQ9bWF1eERlUDQ1NWVz").decode()

if os.path.exists(password_file):
    if os.path.exists(data_file):
        with open(password_file, 'r') as file:
            password_content = file.read().strip()

        if password_content == expected_password:
            final_output = base64.b64decode("bGUgbW90IGRlIHBhc3NlIGVzdCA6IHA0NTVXMHJE").decode()
            print(final_output)
        else:
            print("Mot de passe incorrect")
    else:
        print("Erreur, le fichier data.txt doit être déplacé dans le répertoire de configurations.")
else:
    print("Erreur, le fichier config/password.txt n'existe pas.")
