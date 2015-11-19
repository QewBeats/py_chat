from Client import Client


clientB= Client()

clientB.connect()
clientB.send_message("I am client B")
print(clientB.recv_message())