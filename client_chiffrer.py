import socket

# Paramètres du serveur
HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connecté au serveur. Tapez vos messages (q pour quitter) :")
    while True:
        msg = input(">>> ")
        if msg.lower() == "q":  # Quitter
            break
        client.sendall(msg.encode("utf-8"))
