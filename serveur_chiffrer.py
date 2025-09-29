import socket
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

HOST = "172.20.10.4"
PORT = 15555

# Charger la clé privée depuis un fichier PEM
with open("privatePM.pem", "rb") as f:
    private_key = serialization.load_pem_private_key(f.read(), password=None)
    print("Clé privée chargée")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.bind((HOST, PORT))
    serveur.listen(1)
    print(f"Serveur en attente de connexion sur {HOST}:{PORT}...")

    conn, addr = serveur.accept()
    with conn:
        print(f"Connecté par {addr}")
        while True:
            data = conn.recv(256)  # Limité à un bloc RSA
            if not data:
                break

            try:
                # Déchiffrement RSA
                message = private_key.decrypt(
                    data,
                    padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None
                    )
                )
                print("Message déchiffré :", message.decode("utf-8"))
            except Exception as e:
                print("Erreur de déchiffrement :", e)
