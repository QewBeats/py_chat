from Server import Server
from Client import Client

Server.start()
print("Server is listening...")
while True:
    print(Server.recv_message())
    client_message=input("Server says type message")
    Server.send_message(client_message)





