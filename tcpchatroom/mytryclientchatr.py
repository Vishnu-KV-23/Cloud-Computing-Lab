import socket
import threading
serverIP='127.0.0.1'
serverport=12345
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect((serverIP,serverport))
print("connected to server")

def recvmsgs(clientsocket):
    while True:
        try:
            message=clientsocket.recv(1024).decode('utf-8')
            print("\n"+message)
        except:
            print("an error has occured")
            clientsocket.close()
            break
thread=threading.Thread(target=recvmsgs,args=(clientsocket,))
thread.start()
while True:
    message=input("You:")
    if message=='exit':
        clientsocket.send('exit'.encode('utf-8'))
        clientsocket.close()
        break
    
    clientsocket.send(message.encode('utf-8'))
