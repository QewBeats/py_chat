from Server import Server


Server.start()
print("Server is listening...")
while True:
    print(Server.recv_message())
    client_message=input("Server your turn: ")
    Server.send_message(client_message)





