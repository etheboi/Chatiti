import socket
import random   
from threading import Thread
from datetime import datetime
import colorama
from tkinter import *
from tkinter import ttk
import os
import atexit
import subprocess

colorama.init()
colors = [colorama.Fore.BLUE, colorama.Fore.CYAN, colorama.Fore.GREEN, colorama.Fore.LIGHTBLACK_EX,
          colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTCYAN_EX, colorama.Fore.LIGHTGREEN_EX,
          colorama.Fore.LIGHTMAGENTA_EX, colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTWHITE_EX,
          colorama.Fore.LIGHTYELLOW_EX, colorama.Fore.MAGENTA, colorama.Fore.RED, colorama.Fore.WHITE, colorama.Fore.YELLOW
          ]
client_color = random.choice(colors)
'''
def set_pass():
    global password_file
    if os.path.exists("./password.txt"):
        password = str(entered_password.get())
        os.remove("./password.txt")
        password_file = open("./password.txt", "x")
        password_file.write(password)
        password_file.close()
    else:
        password = str(entered_password.get())
        password_file = open("./password.txt", "x")
        password_file.write(password)
        password_file.close()

def validate_pass():
    entered_password_str = str(entered_password.get())
    if os.path.exists("./password.txt"):
        password = open("./password.txt", "r")
        if entered_password_str == password.read():
            login_win.destroy()
            main_win()
        else:
            entered_password.input("")
    else:
        set_pass()

global login_win
def login_win():
    global login_win
    login_win = Tk()
    login_win.geometry("500x300")
    login_win.title("Chatiti Login")

    global login_label
    login_label = Label(login_win, text="If a password is not set, then enter one to set it.\nElse just enter your set password.")
    login_label.pack()

    global entered_password
    entered_password = Entry(login_win)
    entered_password.pack()

    login_button = Button(login_win, text="Continue", command=validate_pass)
    login_button.pack()
    validate_pass()

    login_win.mainloop()
'''

global main_win
def main_win():
    global win
    win = Tk()
    win.geometry("500x300")
    win.title("Chatiti Launcher")

    Label(win, text="Host IP:").pack()
    global SERVER_HOST_ENT
    SERVER_HOST_ENT = Entry(win)
    SERVER_HOST_ENT.pack()

    Label(win, text="Host Port:").pack()
    global SERVER_PORT_ENT
    SERVER_PORT_ENT = Entry(win)
    SERVER_PORT_ENT.pack()

    Button(win, text="Connect", command=connect).pack()

    global name_label
    name_label = Label(win, text="\n\n\n\nName:")
    name_label.pack()
    global name_ent
    name_ent = Entry(win)
    if os.path.exists("./name.txt"):
        name_file = open("./name.txt", "r")
        name_ent.insert(0, name_file.read())
        name_file.close()
    name_ent.pack()

    win.mainloop()

global connect
def connect():
    name = str(name_ent.get())
    if os.path.exists("./name.txt"):
        os.remove("./name.txt")
        name_file = open("./name.txt", "x")
        name_file.write(name)
        name_file.close()
    else:
        name_file = open("./name.txt", "x")
        name_file.write(name)
        name_file.close()
    if name == "":
        main_win()
        print(f"{colorama.Fore.RED}[*]Error: You must set a name!")
    else:
        global SERVER_HOST
        SERVER_HOST = str(SERVER_HOST_ENT.get())
        global SERVER_PORT
        SERVER_PORT = int(SERVER_PORT_ENT.get())
        win.destroy()
        separator_token = "<SEP>"

        s = socket.socket()
        print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
        s.connect((SERVER_HOST, SERVER_PORT))
        print("[+] Connected.")
        s.send(f"{colorama.Fore.YELLOW}{name} has joined!".encode())

        global leave
        def leave():
            s.send(f"{colorama.Fore.YELLOW}{name} has left!".encode())
            main_win()

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
                leave()
            date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            to_send = f"{client_color}{name}{separator_token}{to_send}{colorama.Fore.RESET}"
            s.send(to_send.encode())

        s.close()

main_win()

atexit.register(leave())