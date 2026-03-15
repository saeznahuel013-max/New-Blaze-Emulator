import socket
import struct
import sys

def crear_respuesta_dns(data, ip_destino):
    ID = data[:2]
    Flags = b"\x81\x80"
    QDCOUNT = data[4:6]
    ANCOUNT = b"\x00\x01"
    NSCOUNT = b"\x00\x00"
    ARCOUNT = b"\x00\x00"
    
    end_of_name = data[12:].find(b'\x00') + 13
    Question = data[12:end_of_name + 4]
    
    Answer = b"\xc0\x0c" + b"\x00\x01" + b"\x00\x01" + struct.pack(">I", 60) + b"\x00\x04"
    IP_Bytes = socket.inet_aton(ip_destino)
    
    return ID + Flags + QDCOUNT + ANCOUNT + NSCOUNT + ARCOUNT + Question + Answer + IP_Bytes

def iniciar_servidor():
    mi_ip = "10.180.85.246" 
    puerto = 53
    
    print("==============================================")
    print("   FIFA REDIRECTOR PRO - VERSION COMPATIBLE   ")
    print("   Redireccionando EA a: " + mi_ip)
    print("==============================================")

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', puerto))
    except Exception as e:
        print("ERROR: No se pudo abrir el puerto 53.")
        print("Detalle: " + str(e))
        print("Recuerda ejecutar el CMD como ADMINISTRADOR.")
        return

    print("Escuchando peticiones... No cierres esta ventana.")
    
    while True:
        data, addr = sock.recvfrom(512)
        print("Peticion recibida de la PS3!")
        respuesta = crear_respuesta_dns(data, mi_ip)
        sock.sendto(respuesta, addr)
        print("Respuesta enviada correctamente.")

if __name__ == "__main__":
    iniciar_servidor()