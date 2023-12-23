import socket
import random
from threading import Thread
from datetime import datetime
import colorama
from tkinter import *
from tkinter import ttk
import sys


colorama.init()

colors = [colorama.Fore.BLUE, colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.LIGHTBLACK_EX,
          colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTGREEN_EX,
          colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTWHITE_EX,
          colorama.Fore.LIGHTYELLOW_EX, colorama.Fore.MAGENTA, colorama.Fore.RED, colorama.Fore.WHITE, colorama.Fore.YELLOW
          ]

client_color = random.choice(colors)



SERVER_HOST = sys.argv[1]
SERVER_PORT = sys.argv[2]

try:
    SERVER_PORT = int(SERVER_PORT)
except:
    print(f"{colorama.Fore.RED}[{colorama.Fore.WHITE}*{colorama.Fore.RED}]Error >> Input must be an integer!")
    exit()

separator_token = "<SEP>"

s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

name = input("Enter your name: ")

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send =  input()
    if to_send.lower() == '/exit':
        exit()
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}{name}{separator_token}{to_send}{colorama.Fore.RESET}"
    s.send(to_send.encode())

s.close()