#server socket this program(server.py) needs to be run prior to client socket program(client.py)
#socket module is used which comes with python packages by default

import socket


#functions for sending and receiving messages
def sending():
  msg = input('server:')
  if len(msg)>0:
    client.send(bytes(msg,"utf-8"))
    print('message sent')

def receiving():
  msg = client.recv(1024)
  if len(msg)>0:
    print(f'client:{msg.decode("utf-8")}')


#creating a socket object, by AF_INET we are using IPv4 protocol and by SOCK_STREAM we are using TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding hostname with port number and enabling listen
s.bind((socket.gethostname(),1234))
s.listen()
print('waiting to establish connection...')
client, address = s.accept()                                  #getting client details if found any
print(f"Connection from {address} has been established!!!")   #printing the details
client.send(bytes("Welcome to the server!!","utf-8"))         #sending a message which is coded into bytes

#chatting starts
print('Chatting starts...')
a=0
a=int(input('enter 1 to continue  or 0 to stop:'))            #user opinion 

while a>0:                                                    #loop for sending  and receivingalternatively
  print('receiving message...')
  receiving()
  sending()
  a=int(input('enter 1 to continue  or 0 to stop:'))

print('Disconnecting...')
client.close()                                                #the connection is closed    
    
