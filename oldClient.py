import socket
import sys
import struct 

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
def main():
    rec_offer()


def rec_offer():
    print(f"{bcolors.HEADER}Client started, listening for offer requests... \n")

    # here we will do the recieving of udp

    sock_UDP = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock_UDP.bind((ip, UDP_port))

    magic,mType,targetPort = struct.unpack('Ibh',sock_UDP.recvfrom(1024)[0]) # buffer size is 1024 bytes
    print(f"{bcolors.OKGREEN}Received message: magic {magic} type {mType} target Port {targetPort}\n")

    if magic == 0xfeedbeef and mType == 0x2:
        sock_UDP.close()
        connec_to_server(targetPort)
# end of UPD section @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ goku

# Connect the socket to the port where the server is listening

def connec_to_server(port):
    sock_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (ip, port)
    print( f'{bcolors.HEADER}connecting to %s port %s \n' % server_address)
    sock_TCP.connect(server_address)

    try:
        
        # startMsg = sock_TCP.recv(104)
        # print(f'{bcolors.OKGREEN} %s"' % startMsg)

        # Send data
        while True: 
            sock_TCP.sendall(bytes(getch(),'UTF-8'))

    finally:
        print(f'{bcolors.FAIL}closing socket \n')
        sock_TCP.close()
        print(f'{bcolors.OKBLUE}Server disconnected, listening for offer requests...')
        rec_offer()

# Create a TCP/IP socket
def getch():
    import termios
    import  tty
    def _getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
    return _getch()


if __name__ == "__main__":
    main()