import socket
import sys

# Create a TCP/IP socket

UDP_IP = "172.1.0.123"
UDP_PORT = 13117
MESSAGE = b"Hello, World!"

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock_UDP = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock_UDP.bind(('172.1.0.123', 3189))
sock_UDP.sendto(MESSAGE, (UDP_IP, UDP_PORT))
# sock_UDP.shutdown(socket.SHUT_RDWR)
sock_UDP.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('172.1.0.123', 3189)



print("Client started, listening for offer requests...")

print(sys.stderr, 'starting up on %s port %s' % server_address)
sock.bind(server_address)


sock.listen(1)

while True:
    # Wait for a connection
    print(sys.stderr, 'waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print(sys.stderr, 'connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print(sys.stderr, 'received "%s"' % data)
            if data:
                print(sys.stderr, 'sending data back to the client')
                connection.sendall(data)
            else:
                print(sys.stderr, 'no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()