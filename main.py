# IMPORTING MODULE
import os, sys, threading, ftplib, socket, time, base64
from module.color import color

# VARIABLE
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LHOST = str(sys.argv[2])
LPORT = 21
RPORT = 20


# FONCTION
with open('./banner.deco', 'r') as PB:
    banner = PB.read()

def arg():
    if sys.argv[1] != '-a':
        print(f' {color.bold_on}pyFTPHoneypot{color.reset}, a simple FTP honeypot write in python3:\n   -a : Specify the your address or the network interface to use.\n\n   Example: python3 ./main.py -a 127.0.O.1\n            python3 ./main.py -a wlan0')
        sys.exit()
    elif sys.argv[1] == '-a':
        pass

def start():
    x = 0
    print(f'{color.fr_green} [+] The FTP honeypot server is up on {LHOST}:{LPORT}{color.reset}')
    s.bind((LHOST, LPORT))
    while True:
        x += 1
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            print(f' [!] New connection from {addr}')
            while True:
                data = conn.recv(1024)
                if not data: break
                conn.sendall(data)
        if x == 1000:
            break

def main():
    from module.creat_struct import struct
    arg()
    struct()
    start()


# EXECUTE
if __name__ == '__main__':
    try:
        print(color.fr_purple, banner, f'\n{color.reset}')
        main()
    except KeyboardInterrupt:
        print(f'\033[A\n{color.fr_red} [!] Keyboard interrupt keys pressed{color.reset}')