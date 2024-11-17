import socket
import threading
serverip='127.0.0.1'
serverport=12345
clients=[]
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serversocket.bind((serverip,serverport))
serversocket.listen()
def broadcastmsgs(message,clientsocket):
    for client in clients:
        if client!=clientsocket:
            try:
                send(message.encode('utf-8'))
            except:
                print("an error has occured")
                clients.remove(clientsocket)
def handleclients(clientsocket,clientaddress):
    print(f"welcome to the party {clientaddress}")
    while True:
        try:
            message=clientsocket.recv(1024).decode('utf-8')
            print(f"{clientaddress}:{message}")
            broadcastmsgs(message,clientsocket)
        except:
            print("some error has occured")
            clientsocket.close()
            clients.remove(clientsocket)
            break
print(f"the chatroom service started at {serverip}:{serverport}")
while True:
    clientsocket,clientaddress=serversocket.accept()
    clients.append(clientsocket)
    thread=threading.Thread(target=handleclients,args=(clientsocket,clientaddress))
    thread.start()


