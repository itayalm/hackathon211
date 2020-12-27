import socket
import sys
import time

import struct
TARGET_ip = '172.1.0.123'
TARGET_port = 13117 
TCP_port = 3189 
TIME_BETWEEN_OFFERS = 1

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

def main():
    while True:
        send_offer(TARGET_ip, TARGET_port)
    # create thread for sending udp
    # create thred for recieving and handling tcp
    # plus minus

# def send_offer(thread_name, ip, port):
#     UDP_IP = ip
#     UDP_PORT = port
#     datagram = struct.pack('Ibh',0xfeedbeef, 0x2, TCP_port)

#     while True:
#         print(f"{bcolors.HEADER}Thread %s: UDP target IP: %s \n" % (thread_name,  UDP_IP))
#         print(f"{bcolors.HEADER}Thread %s: UDP target port: %s \n" % (thread_name, UDP_PORT))
#         print(f"{bcolors.OKCYAN}Thread %s: message: %s \n" % (thread_name, datagram))

#         sock_UDP = socket.socket(socket.AF_INET, # Internet
#                             socket.SOCK_DGRAM) # UDP
#         # sock_UDP.bind(('172.1.0.123', OUR_PORT))
#         sock_UDP.sendto(datagram, (UDP_IP, UDP_PORT))
#         # sock_UDP.shutdown(socket.SHUT_RDWR)
#         sock_UDP.close()
#         time.sleep(TIME_BETWEEN_OFFERS)


def send_offer(ip, port):
    UDP_IP = ip
    UDP_PORT = port
    # while True:
    datagram = struct.pack('Ibh',0xfeedbeef, 0x2, TCP_port)
    print(f"{bcolors.HEADER}UDP target IP: %s \n" % UDP_IP)
    print(f"{bcolors.HEADER}UDP target port: %s \n" % UDP_PORT)
    print(f"{bcolors.OKCYAN}message: %s \n" % datagram)

    sock_UDP = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock_UDP.sendto(datagram, (UDP_IP, UDP_PORT))
    # sock_UDP.shutdown(socket.SHUT_RDWR)
    sock_UDP.close()
    start_tcp(ip,TCP_port)


# Create a TCP/IP socket
def start_tcp(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to the port
    server_address = (ip, port)

    print(f"{bcolors.HEADER}Client started, listening for offer requests... \n")
    print(f'{bcolors.HEADER}starting up on %s port %s \n' % server_address)
    sock.bind(server_address)


    sock.listen(1)

    # Wait for a connection
    print(f'{bcolors.HEADER}waiting for a connection  \n')
    connection, client_address = sock.accept()

    try:
        print(f'{bcolors.OKGREEN}connection from \n', client_address)

        # Receive the data in small chunks and retransmit it
        startTime = time.time()
        while True:
            curTime = time.time()
            print(curTime, " ", startTime, " ", curTime- startTime)
            if((curTime - startTime) > 2.0):
                break
            data = connection.recv(16)
            if (data == b''):
                raise RuntimeError("Hi tommer!")
            print(f'{bcolors.OKBLUE}received "%s" \n' % data)
            # if data:
            #     print(f'{bcolors.OKGREEN}sending data back to the client \n')
            #     connection.sendall(data)
            # else:
            #     print(f'{bcolors.OKBLUE}no more data from \n', client_address)
            #     break
            
    finally:
        # Clean up the connection
        connection.close()
        sock.shutdown(socket.SHUT_RDWR)
        
if __name__ == "__main__":
    main()

    