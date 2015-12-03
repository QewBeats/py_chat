from Server import Server


Server.start()
print("Server is listening...")
while True:
    print(Server.recv_message())
    client_message=input("Server your turn: ")
    Server.send_message(client_message)
lient [Algorithm]
1. Create a Client
2. Give the client an identity , The identity should be the  Unique ID
3. Connect the client to the server
4. Wait for the server to send a command

Client Send Message [Algorithm]
1. Send six message frame
    Frame[0] = Unique ID 
        Frame[1] = Delimiter (Should be and empty Frame)
            Frame[2] = Details about the client [This should be an xml Document, see  client Detail for further information]
                Frame[3] = Delimiter (Should be and empty Frame)
                    Frame[4] = Type of Message Been Sent e.g File,ScreenShot [ The type should be kept short to prevent data wastage ] 
                        Frame[5] = Delimiter (Should be and Empty Frame)
                            Frame[6] = Payload [The message itself]


                            Client Details [Algorithm]
                            1. The clients details should be an XML format string  containing  the ComputerName,Username,UniqueID and IPAddress
                            2. Every message (Frame) sent will contain the ID of the Client in Frame[0] and the client Details in Frame[2] 


                            Client Receive Message [Algorithm]
                            1.Client determine and verify the identity in Frame[0] to make sure the message is for him
                            2.Client extract message at frame[2]
                            3. Client Act on message


                            Server Connection [Algorithm]
                            This is an Algorithm for the server
                            1. Setup the connection with RouterSocket
                            2. Upon client connect get their identity at frame[0] and save it in a HashTable as the Key
                            3. Extract Frame[3] which is a full detail about the client as the Value of the hash table
                            4. Use the Identity to identify the client 
                            5


                            Sever Received Message [Algorithm]
                            1.Extract the Id at Frame[0]
                            2.Extract Client Details at Frame[2]
                            3. If Id (Frame[0]) not in hashTable add it as key 
                            4.Add Client Details Frame[2] as Value
                            5. Determine Message Type Frame[4]
                            6. Extract Message Frame[6]

                            Server Send Message [Algorithm]
                            1. Identify the client name from the HashTable 
                            2. Encode the clients Identity on frame[0]
                            3. Encode the message type on frame[2]
                            4. Encode the message on frame[4] 
                            5. Send the message

                            




