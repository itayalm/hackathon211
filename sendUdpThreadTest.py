import logging
import threading
import time
import socket

TARGET_ip = '172.1.0.123'
TARGET_port = 13118

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


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


def send_offer_thread(name, ip, port):
    UDP_IP = ip
    UDP_PORT = port
    MESSAGE = b"Hello, World!"
    while True:
        OUR_PORT = 3189
        logging.info(f"{bcolors.HEADER}Thread %s: UDP target IP: %s \n" % (name,  UDP_IP))
        logging.info(f"{bcolors.HEADER}Thread %s: UDP target port: %s \n" % (name, UDP_PORT))
        logging.info(f"{bcolors.OKCYAN}Thread %s: message: %s \n" % (name, MESSAGE))

        sock_UDP = socket.socket(socket.AF_INET, # Internet
                            socket.SOCK_DGRAM) # UDP
        # sock_UDP.bind(('172.1.0.123', OUR_PORT))
        sock_UDP.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        # sock_UDP.shutdown(socket.SHUT_RDWR)
        sock_UDP.close()
        time.sleep(name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=send_offer_thread, args=(1,TARGET_ip, TARGET_port))
    y = threading.Thread(target=send_offer_thread, args=(2,TARGET_ip, TARGET_port))
    logging.info("Main    : before running thread")
    x.start()
    y.start()
    logging.info("Main    : wait for the thread to finish")
    x.join()
    logging.info("Main    : all done")