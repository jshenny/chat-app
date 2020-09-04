from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

HOST = ''
PORT = 5500
BUFSIZ = 1024
ADDR = (HOST, PORT)

def wait_for_connection(SERVER):
    run = True
    while run:


# a server has a bind() method which binds it to a specific port so it can
# listen to incoming requests on that ip and port
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)

# listen() puts the server into listening mode so it can listen to incoming 
# connections
if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    ACCEPT_THREAD = Thread(target=wait_for_connection, (SERVER))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

