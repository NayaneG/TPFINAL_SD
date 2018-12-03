
PORTA  = 1234               # porta
GRUPO4 = '224.0.0.251'      # endereco multicast

TTL = 1                   # time to live
timeout = 3
import os
import time
import struct
import socket
import sys
import select


def main():
    grupo = GRUPO4

    palavra = input('Entre com -s para servidor e -c para cliente trouxa')
    if "-s" in palavra:
        print('Olá servidor otário')
        envia(grupo)
    else:
        print('Olá cliente otário')
        recebe(grupo)


def envia(grupo):
    UDP_IP = "224.3.1.1"
    UDP_PORT = 5005
    buf = 1024
    file_name = 'teste.txt'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
    print("Sending %s ..." % file_name)

    f = open(file_name, "r")
    data = f.read(buf)
    while (data):
        if (sock.sendto(data.encode(), (UDP_IP, UDP_PORT))):
            data = f.read(buf)
            time.sleep(0.02)  # Give receiver a bit time to save

    sock.close()
    f.close()


def recebe(grupo):
    UDP_IP = "127.0.0.1"
    IN_PORT = 5005
    timeout = 3

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_IP, IN_PORT))

    while True:
        data, addr = sock.recvfrom(1024)
        if data:
            print("File name:", data)
            file_name = data.strip()
        f = open('testefinal.txt', 'wb')

        while True:
            ready = select.select([sock], [], [], timeout)
            if ready[0]:
                data, addr = sock.recvfrom(1024)
                f.write(data)
            else:
                print("%s Finish!" % file_name)
                f.close()
                break


if __name__ == '__main__':
    main()