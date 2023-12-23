import subprocess

global SERVER_HOST
global SERVER_PORT
global chatiti_server
def chatiti_server(SERVER_HOST, SERVER_PORT):
    import socket
    from threading import Thread

    hostname = socket.gethostname()
    userip = socket.gethostbyname(hostname)

    if SERVER_HOST != userip:
        print("[*] Error: Entered IP address is not matching with current address")
        exit()

    global separator_token
    separator_token = "<SEP>"

    global client_sockets
    client_sockets = set()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")
        client_sockets.add(client_socket)
        t = Thread(target=listen_for_client, args=(client_socket,))
        t.daemon = True
        t.start()

    for cs in client_sockets:
        cs.close()
    s.close()

def listen_for_client(cs):
    while True:
        try:
            global msg
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            client_socket.send(msg.encode())