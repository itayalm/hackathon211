
import sys
import tty
import termios
from signal import signal, SIGINT

# def getch():
#     import termios
#     import  tty
#     def _getch():
#         fd = sys.stdin.fileno()
#         old_settings = termios.tcgetattr(fd)
#         try:
#             tty.setraw(fd)
#             ch = sys.stdin.read(1)
#             if ch == '\x03' : sys.exit(0)
#         finally:
#             termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#         return ch
    # return _getch()
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
while True : 
    print(getch())
    
# print(ch)
# hi tommer

# from signal import signal, SIGINT
# from sys import exit

# def handler(signal_received, frame):
#     # Handle any cleanup here
#     print('SIGINT or CTRL-C detected. Exiting gracefully')
#     exit(0)

# if __name__ == '__main__':
#     # Tell Python to run the handler() function when SIGINT is recieved
#     signal(SIGINT, handler)

#     print('Running. Press CTRL-C to exit.')
#     while True:
#         # Do nothing and hog CPU forever until SIGINT received.
#         pass