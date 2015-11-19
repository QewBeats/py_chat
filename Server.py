import zmq
import time

class Server():

     # first create a context it is required

    context=None
    socket=None

    # create a response socket [Response socket are mostly for serves ]


    @staticmethod
    def start():
        Server.context = zmq.Context()
        Server.socket = Server.context.socket(zmq.REP)
        Server.socket.bind("tcp://*:2000")

    # listen on tcp port 2000
        #self.socket.bind("tcp://*:2000")
       # yan="3"
    @staticmethod
    def send_message(message):
        Server.socket.send_string(message)

    @staticmethod
    def recv_message():

        return Server.socket.recv_string()








    #while True:
    # wait for next request from client
    # will block till a message is received from the clien
    #print("client says",recv_message())
    #send_message("servers greet you")

