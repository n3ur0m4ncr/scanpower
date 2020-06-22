import socket 
import sys
import os

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan    = "\033[96m"
END = '\033[0m'

if len(sys.argv) < 2:
    os.system("clear || cls")
    sys.stdout.write(RED + """  
  
    

███████╗ ██████╗ █████╗ ███╗   ██╗      ██████╗  ██████╗ ██╗    ██╗███████╗██████╗ 
██╔════╝██╔════╝██╔══██╗████╗  ██║      ██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔══██╗
███████╗██║     ███████║██╔██╗ ██║█████╗██████╔╝██║   ██║██║ █╗ ██║█████╗  ██████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║╚════╝██╔═══╝ ██║   ██║██║███╗██║██╔══╝  ██╔══██╗
███████║╚██████╗██║  ██║██║ ╚████║      ██║     ╚██████╔╝╚███╔███╔╝███████╗██║  ██║
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═╝      ╚═════╝  ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝
                                                                                   
                                                                                          
    """  + END+BLUE+'GitHub: https://github.com/shangow'.format(RED, END).center(69) +
    '\n' + '\tAutor: {}shangow'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
    '\n' + '\tVersion: {}1.0{}\n'.format(YELLOW, END).center(80) + '\n')
else:
    sys.exit('Usage: python scan.py')
    os.system("clear || cls")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(1)

host = input("[*] Digite o host que deseja escanear: ")

def portscanner(port):
    if sock.connect_ex((host, port)):
            print("[!!] Porta  %d esta fechada") % (port)
    else: 
            print("[*] Porta %d esta aberta") % (port)
for port in range (1, 100): 
         portscanner(port)

    