import socket
import sys


def main():
    rec_offer("172.1.0.123", 13117)

def connec_to_server(ip, port):
    sock_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = (ip, port)
    print(sys.stderr, 'connecting to %s port %s' % server_address)
    sock_TCP.connect(server_address)

    try:
        
        # Send data
        message = b'This is the message.  It will be repeated.'
        print(sys.stderr, 'sending "%s"' % message)
        sock_TCP.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock_TCP.recv(16)
            amount_received += len(data)
            print(sys.stderr, 'received "%s"' % data)

    finally:
        print(sys.stderr, 'closing socket')
        sock_TCP.close()


# Create a TCP/IP socket

def rec_offer(ip,port):
    print("Client started, listening for offer requests...")

    # here we will do the recieving of udp

    UDP_IP = ip
    UDP_PORT = port

    sock_UDP = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock_UDP.bind((UDP_IP, UDP_PORT))

    data, addr = sock_UDP.recvfrom(1024) # buffer size is 1024 bytes
    print(f'received message: {data} from addr {addr}')
    ip, port = addr
    connec_to_server(ip, port)
# end of UPD section @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ goku

# Connect the socket to the port where the server is listening

if __name__ == "__main__":
    main()
    