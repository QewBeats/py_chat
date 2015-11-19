from Client import Client


clientB= Client()

clientB.connect()

while True:
    user_input=input("Type message")
    clientB.send_message(user_input)
    print(clientB.recv_message())