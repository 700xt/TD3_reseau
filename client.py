import socket

# Paramètres du serveur
HOST = "172.20.10.10"
PORT = 15555

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connecté au serveur. Tapez vos messages (q pour quitter) :")
    while True:
        msg = input(">>> ")
        if msg.lower() == "q":  # Quitter
            break
        client.sendall(msg.encode("utf-8"))
