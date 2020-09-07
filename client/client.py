from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time

class Client:
    """ For communication with server """
HOST = 'localhost'
PORT = 5500
ADDR = (HOST, PORT)
BUFSIZ = 512
