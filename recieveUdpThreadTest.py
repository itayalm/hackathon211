import logging
import threading
import time
import socket

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



def recieve_udp_thread(name, ip , port):
    while True:
        print(f"{bcolors.HEADER}Client started, listening for offer requests... \n")

        # here we will do the recieving of udp

        UDP_IP = ip
        UDP_PORT = port

        sock_UDP = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
        sock_UDP.bind((UDP_IP, UDP_PORT))

        data, addr = sock_UDP.recvfrom(1024) # buffer size is 1024 bytes
        print(f"{bcolors.OKGREEN}Received message: {data} from addr {addr} \n")


        # end of UPD section @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ goku

        # Connect the socket to the port where the server is listening



if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=recieve_udp_thread, args=(1,'172.1.0.123', 13118))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")