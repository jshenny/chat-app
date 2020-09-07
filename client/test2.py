from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)
messages = []

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            messages.append(msg)
            print(msg)
        except Exception as e:
            print("[EXCEPTION]", e)
            break

def send_message(msg):
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()

receive_thread = Thread(target=receive_messages)
receive_thread.start()

send_message("Bob")
time.sleep(10)
send_message("hello")
time.sleep(2)
send_message("{quit}")