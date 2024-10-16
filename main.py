#!/bin/env python3

# IMPORTING MODULE
import os, sys, threading, ftplib, socket, time, base64, string
from module.color import color
import netifaces as ni

# VARIABLE
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
LHOST = str(sys.argv[2])
LPORT = 21
RPORT = 20

# CHECK IF LHOST IS AN INTERFACE
if LHOST and LHOST[0].islower():
    LHOST = ni.ifaddresses(LHOST)[ni.AF_INET][0]['addr']
else:
    pass

# BANNER
with open('./banner.deco', 'r') as TMP:
    banner = TMP.read()

def arg():
    if sys.argv[1] != '-a':
        print('\033[A\033[A')
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
        # TO REMOVE WHEN IT'S FINISH
        choise = input(f'{color.fr_red} ⚠️ THIS PROGRAM IS NOT FINISH, IF YOU NEED AN HONEYPOT GO TO THE AWESOME HONEYPOTS REPO, PRESS Y TO EXECUTE ! ⚠️\n{color.reset}')
        if choise == 'Y' or choise == 'y':
            main()
        else:
            print(f'\033[A\n{color.fr_red} [!] ABORDING ...{color.reset}')
    except KeyboardInterrupt:
        print(f'\033[A\n{color.fr_red} [!] Keyboard interrupt keys pressed{color.reset}')