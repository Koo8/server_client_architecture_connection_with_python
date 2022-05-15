'''
    This is the server, wait for receiving requests from clients
'''
import socket

# use this local computer as the server, 
# cmd->ipconfig->ipv4 address can also mannually get the address
host = socket.gethostbyname(socket.gethostname())
# use a port number outside the 'well-known's
port = 8989

# create a socket for connecting to clients, 
# not for talking to clients. 
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tcp
# bind to a tuple
socket.bind((host, port))
# queue up max 5 connect requests b4 refusing outside connections.
socket.listen(5)

# run server infitely
while True:
    # wait and accept requests from clients, a new socket is created
    # for talking to this client with the ip address
    (newlycreatedsocketforclient, clientIPaddress) = socket.accept()
    # receive message from client
    msg = newlycreatedsocketforclient.recv(1024) # bytes
    # decode msg for human
    decoded_msg = msg.decode('utf-8')
    # to send message to the client, use encode() 
    newlycreatedsocketforclient.send(f"Thank you for your info: {decoded_msg}".encode())

    # server can be closed if needed
    # newlycreatedsocketforclient.close()

