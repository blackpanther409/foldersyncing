#server socket this program(server.py) needs to be run prior to client socket program(client.py)
#socket module is used which comes with python packages by default

import socket


#functions for sending and receiving messages
def sending():
  msg = input('server:')
  global a
  if msg.lower().strip()=='bye':
    a=0
  if len(msg)>0:
    client.send(bytes(msg,"utf-8"))
    print('message sent')

def receiving():
  msg = client.recv(1024)
  msg = msg.decode("utf-8")
  global a
  if msg.lower().strip()=='bye':
    a=0
  if len(msg)>0:
    print(f'client:{msg}')


#creating a socket object, by AF_INET we are using IPv4 protocol and by SOCK_STREAM we are using TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding hostname with port number and enabling listen
s.bind((socket.gethostname(),1234))

i=1
while i==1:
    s.listen()
    print('waiting to establish connection...')
    client, address = s.accept()                                  #getting client details if found any
    print(f"Connection from {address} has been established!!!")   #printing the details
    client.send(bytes("Welcome to the server!!","utf-8"))         #sending a message which is coded into bytes

    #chatting starts
    print('Chatting starts...')
    a=0
    a=int(input('Press 1 to accept the connection(any other key to reject):'))            #user opinion 

    while a==1:                                                    #loop for sending  and receivingalternatively
      print('receiving message...')
      receiving()
      if a!=1:
        break
      sending()
    print(f'User:{address[0]} disconnected from the chat')
    client.close()                                                #the connection is closed
    i=int(input('Enter 1 to stay online:'))
    
print('Closing server..')
