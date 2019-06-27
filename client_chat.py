#client socket

import socket

#functions for sending and receiving messages
def sending():
  msg = input('client:')
  global a
  if 'bye' in msg.lower().strip():
    a=0
  if len(msg)>0:
    s.send(bytes(msg,"utf-8"))
    print('message sent')

def receiving():
  msg = s.recv(1024)
  msg = msg.decode("utf-8")
  global a
  if 'bye' in msg.lower().strip():
    a=0
  if len(msg)>0:
    print(f'server:{msg}')
    
#creating a socket object, by AF_INET we are using IPv4 protocol and by SOCK_STREAM we are using TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#give the ip address of the server device you wanted to connect to, to the host variable
#host='192.168.0.106'          
host=socket.gethostname()                                 #getting local host address, when you wanted your local host to be the server socket


s.connect((host,1234))                                    #establishing connection with a server on 1234

msg = s.recv(1024)                                        #getting a default message of welcome from server
print(f'server:{msg.decode("utf-8")}')

#chatting starts
print("Chatting starts...")
a=0
a=int(input('Press 1 to accept the connection(any other key to reject):'))        #user opinion 

while a==1:
  sending()                                               #sending message
  if a!=1:
    break
  try:
    print('receiving message...')                         #loop for receiving and sending alternatively
    receiving()                                           #receiving message
  except ConnectionAbortedError:                          #error handling incase connection is forcibly closed         
    break
print(f'User:{host} disconected from the chat')
s.close()                                                 #the connection is closed
