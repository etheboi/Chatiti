import glob
from tkinter import *
from tkinter import ttk
import os
from time import sleep
import requests
import subprocess

global file_location
file_location = "C:/Chatiti"

#file location
def installer_2_open():
    global installer_2
    installer_2 = Tk()
    installer_2.title("Chatiti Installer")
    installer.destroy()
    installer_2.geometry("500x300")
    install_info = Label(installer_2, text="WARNING\nWhen you install this, 2 packages will be installed:\ncolorama\npyinstaller").pack()
    Label(installer_2, text="\nFile Location:").pack()
    global file_location_ent
    file_location_ent = Entry(installer_2)
    file_location_ent.insert(0, f"{file_location}")
    file_location_ent.pack()
    Button(installer_2, text="Download", command=create_files).pack()
    installer_2.mainloop()


#generate files
def create_files():
    installer_2.destroy
    subprocess.run(["pip", "install", "colorama"])
    subprocess.run(["pip", "install", "pyinstaller"])
    if os.path.exists(file_location):
        url = "https://chatiti.netlify.app/raw/chatiti"
        r = requests.get(url, allow_redirects=True)
        open(f'{file_location}/Chatiti.py', 'wb').write(r.content)

        url = "https://chatiti.netlify.app/raw/readme"
        r = requests.get(url, allow_redirects=True)
        open(f'{file_location}/README.txt', 'wb').write(r.content)
    else:
        os.mkdir(file_location)
        url = "https://chatiti.netlify.app/raw/chatiti"
        r = requests.get(url, allow_redirects=True)
        open(f'{file_location}/Chatiti.py', 'wb').write(r.content)

        url = "https://chatiti.netlify.app/raw/readme"
        r = requests.get(url, allow_redirects=True)
        open(f'{file_location}/README.txt', 'wb').write(r.content)

    os.chdir(file_location)
    subprocess.run([f"pyinstaller", "./Chatiti.py", "--onefile"])


#main-installer
installer = Tk()
installer.geometry('500x300')
installer.title("Chatiti Installer")
next_1 = Button(installer, text = 'Next', command = installer_2_open)
next_1.place(x=300, y=230)
text_1 = Label(installer, text="Chatiti Installer\nClick Next to continue with setup")
text_1.place(x=225, y=90)
installer.mainloop()