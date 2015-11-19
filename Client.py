import zmq
import sys

context = zmq.Context()
print ("Connecting  to server")
socket = context.socket(zmq.REQ)
socket.connect("tcp://127.0.0.1:2000")

for request in range(1,10):
    print("Sending Request ", request)
    socket.send("hello")

    #Get reply
    message = socket.recv()
    print("Server says " , message)

