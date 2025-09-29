import socket

# Paramètres de connexion
HOST = "172.20.10.4"   # Localhost
PORT = 15555         # Port d'écoute (au choix, >1024)

# Création du socket serveur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serveur:
    serveur.bind((HOST, PORT))
    serveur.listen(1)
    print(f"Serveur en attente de connexion sur {HOST}:{PORT}...")

    conn, addr = serveur.accept()
    with conn:
        print(f"Connecté par {addr}")
        while True:
            data = conn.recv(1024)  # Réception de données (max 1024 octets)
            if not data:  # Si plus de données, on arrête
                break
            print("Reçu :", data.decode("utf-8"))
