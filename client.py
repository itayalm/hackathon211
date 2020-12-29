import socket
import sys
import tty
import termios
import struct 
import asyncio 
import threading
import select 
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m' 
ip = "172.1.0.123"
UDP_port = 13117

def rec_offer():
    print(f"{bcolors.HEADER}Client started, listening for offer requests... \n")

    # here we will do the recieving of udp

    sock_UDP = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock_UDP.bind((ip, UDP_port))

    data = sock_UDP.recvfrom(1024) # buffer size is 1024 bytes
    magic,mType,targetPort = struct.unpack('Ibh',data[0])
    udp_ip = data[1][0]
    print(f"{bcolors.OKGREEN}Received offer from {udp_ip} attempting to connect  \n")
    print(f"{bcolors.OKGREEN}Received message: magic {magic} type {mType} target Port {targetPort} DELETE THIS \n")

    if magic == 0xfeedbeef and mType == 0x2:
        sock_UDP.close()
        try:
            connec_to_server(targetPort,udp_ip)
        except ConnectionRefusedError: 
            rec_offer()
# end of UPD section @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ goku

# Connect the socket to the port where the server is listening

def connec_to_server(port, tip):
    sock_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # sock_TCP.setblocking(0)
    server_address = (tip, port)
    print( f'{bcolors.HEADER}connecting to %s port %s \n' % server_address)
    sock_TCP.connect(server_address)
    try:
        game_mode(sock_TCP)
    finally:
        print(f'{bcolors.FAIL}closing socket \n')
        sock_TCP.close()
        print(f'{bcolors.OKBLUE}Server disconnected, listening for offer requests...')
        rec_offer()
def game_mode(socket):
    
    socket.sendall(bytes('PussyOren\n','UTF-8'))
    # sendThread = threading.Thread(target = rec, args =(socket))
    # receiveThread = threading.Thread(target = send, args =(socket))
    startMsg = socket.recv(1024)
    print(f'{bcolors.OKGREEN} %s"' % startMsg)
    while True:
        socket.sendall(bytes(getch(),'UTF-8'))

    # Send data
    # sendThread.start()
    # receiveThread.start()

async def rec(socket):
    while True:
        data = socket.recv(1024)
        print(data)
def send(socket):
    while True:
        socket.sendall(bytes(getch(),'UTF-8'))
# Create a TCP/IP socket
def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        data = sys.stdin.read(1)
        if data == '\x03' : sys.exit(0)
        return data
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)


if __name__ == "__main__":
    rec_offer()
