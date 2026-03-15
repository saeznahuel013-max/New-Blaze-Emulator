import socket
import threading

def handle_client(client_socket):
    print(f"[+] Conexión recibida de la PS3")
    # Aquí es donde el FIFA 15 enviaría datos
    # Por ahora, mantenemos la conexión abierta para que no dé error
    data = client_socket.recv(1024)
    print(f"[*] Datos recibidos: {data}")
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 42124))
    server.listen(5)
    print("[*] Servidor Blaze FIFA 15 escuchando en el puerto 42124...")

    while True:
        client, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
