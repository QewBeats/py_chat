import zmq
import time


# first create a context it is required
context = zmq.Context()

# create a response socket [Response socket are mostly for serves ]
socket = context.socket(zmq.REP)

# listen on tcp port 2000
socket.bind("tcp://*:2000")


while True:
    # wait for next request from client
    # will block till a message is received from the client
    message = socket.recv()
    print("The message from client is :", message)
    time.sleep(1)
    socket.send("Server says hi")



