from tkinter import *
from source import chatiti_server

global SERVER_HOST
global SERVER_PORT

global open_server
def open_server():
    SERVER_HOST = str(SERVER_HOST_ENT.get())
    SERVER_PORT = int(SERVER_PORT_ENT.get())
    win.destroy()
    print(f"[*] Attempting to open server {SERVER_HOST}:{SERVER_PORT}")
    chatiti_server(SERVER_HOST, SERVER_PORT)

win = Tk()
win.geometry("500x300")
win.title("Chatiti CreateServer")
Label(win, text="Host IP:").pack()
SERVER_HOST_ENT = Entry(win)
SERVER_HOST_ENT.pack()
Label(win, text="Host Port:").pack()
SERVER_PORT_ENT = Entry(win)
SERVER_PORT_ENT.pack()
Button(win, text="Open server", command=open_server).pack()
win.mainloop()