import socket # for connecting
from colorama import init, Fore
import sys
import os

BLUE = '\33[94m'
LightBlue = '\033[94m'
RED = '\033[91m'
WHITE = '\33[97m'
YELLOW = '\33[93m'
GREEN = '\033[32m'
LightCyan = "\033[96m"
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


    """ + END + BLUE + 'GitHub: https://github.com/shangow'.format(RED, END).center(69) +
                     '\n' + '\tAutor: {}shangow'.format(YELLOW, RED, YELLOW, BLUE).center(76) +
                     '\n' + '\tVersion: {}2.0{}\n'.format(YELLOW, END).center(80) + '\n')
else:
    sys.exit('Usage: python scan.py')
    os.system("clear || cls")
# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def is_port_open(host, port):

    s = socket.socket()
    try:

        s.connect((host, port))

        s.settimeout(0.2)
    except:

        return False
    else:

        return True


host = input("Enter the host:")

for port in range(80, 81):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} is open      {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
