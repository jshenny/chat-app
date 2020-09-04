from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
from person import Person
import time

# GLOBAL CONSTANTS
HOST = 'localhost'
PORT = 5500
BUFSIZ = 512
ADDR = (HOST, PORT)
MAX_CONNECTIONS = 10

# GLOBAL VARIABLES
persons = []
# a server has a bind() method which binds it to a specific port so it can
# listen to incoming requests on that ip and port
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

def broadcast(msg, name):
    # send new messages to all clients
    for person in persons:
        client = person.client
        client.send(bytes(name + ":", "utf8") + msg)

def client_communication(person): # takes client socket as argument
    # handles a single client connection
    client = person.client
    
    # get person's name
    name = client.recv(BUFSIZ).decode("utf8")
    welcome = f"Welcome {name}!"
    client.send(bytes(welcome, "utf8"))

    msg = f"{name} has joined the chat!"
    broadcast(msg)

    while True:
        try:
            msg = client.recv(BUFSIZ)
            print(f"{name}: ", msg.decode("utf8"))

            if msg == bytes("{quit}", "utf8"):
                broadcast(f"{name} has left the chat...", '')
                client.send(bytes("{quit}", "utf8"))
                client.close()
                persons.remove(person)
                break
            else:
                broadcast(msg, name)
        except Exception as e:
            print("[Exception]", e)
            run = False
            break


def wait_for_connection():
    ''' 
    Wait for connection from new clients, start new thread once connected
    :param SERVER: SOCKET
    :return:
    '''
    run = True
    while run:
        try: 
            client, addr = SERVER.accept()
            person = Person(addr, client)
            persons.append(person)
            print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
            Thread(target=client communication, args=(person,)).start()
        except Exception as e:
            print("[FAILURE]", e)
            run = False

    print("SERVER CRASHED")

# listen() puts the server into listening mode so it can listen to incoming 
# connections
if __name__ == "__main__":
    SERVER.listen(MAX_CONNECTIONS) # listen for connections
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

