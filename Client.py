import zmq



class Client():



        def __init__(self):
            self.context = zmq.Context()
            self.socket =self.context.socket(zmq.REQ)


        def connect(self):
            self.socket.connect("tcp://127.0.0.1:2000")

        def send_message(self,message):
            self.socket.send_string(message)


        def recv_message(self):
            return self.socket.recv_string()




