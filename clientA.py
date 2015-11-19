from Client import Client


clientA= Client()

clientA.connect()

while True:
    user_input=input("Type message")
    clientA.send_message(user_input)
    print(clientA.recv_message())