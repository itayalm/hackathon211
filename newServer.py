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



import socket
import threading
import time 
import struct

time_is_up_flag = False
time_is_up_lock = threading.Lock()

# Connection Data
host = '172.1.0.123'
port = 3189
port_to_send_udp = 13116

# starting server 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.setblocking(False)
server.listen()

# Lists for clients 
# List of client sockets
clients = []
# List of names of teams, each index of team name corresponds to the team with the same index in the clients list
team_names = []
# List of addresses to which we should send offer messages to
offer_list = []

# send message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# handling messages from clients
def handle(client):
    while True:
        try:
            message = client.recv(16)
            if (message == b''):
                raise RuntimeError("Hi tommer!")
            print(f'{bcolors.OKBLUE}received "%s" \n' % message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            team_name = team_names[index]
            print('{} left!'.format(team_name).encode('ascii'))
            team_names.remove(team_name)
            break


     
#counting 10 seconds
def count_ten_seconds ():
    time.sleep(10)
    time_is_up_lock.acquire()
    time_is_up_flag = True


# recieving / listening function
def recieve():
    while True:
        #accept connection
        udp_offer_thread = threading.Thread(target = send_offers_for_10_sec, args= ())
        udp_offer_thread.start()
        count_ten_seconds_thread = threading.Thread(target = count_ten_seconds)
        count_ten_seconds_thread.start()
        while time_is_up_lock.locked() == False:
            client, address = server.accept()
        print("Ten seconds finished")
        time_is_up_lock.release()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        print("sned nameee")
        client.send("Sned Mi TEEM name PLZ".encode('ascii'))
        team_name = client.recv(1024).decode('ascii')
        team_names.append(team_name)
        clients.append(client)

        # print team name
        print("Team Name is {}".format(team_name))

        #start handling thread for client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
   
def send_offers_for_10_sec():
    # UDP_IP = ip
    # UDP_PORT = port
    
    udp_socket_out = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    for i in range(0,10):
        for addr in offer_list:
            datagram = struct.pack('Ibh',0xfeedbeef, 0x2, port)
            print(f"{bcolors.HEADER}UDP target IP: %s \n" % port_to_send_udp)
            print(f"{bcolors.HEADER}UDP target port: %s \n" % port_to_send_udp)
            print(f"{bcolors.OKCYAN}message: %s \n" % datagram)
            udp_socket_out.sendto(datagram, addr)
            # sock_UDP.shutdown(socket.SHUT_RDWR)
        time.sleep(1)
        
    udp_socket_out.close()




def main():
    offer_list.append(('172.1.0.123', 13117))

    recieve()





if __name__ == "__main__":
    main()
