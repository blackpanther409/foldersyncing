#client socket

import socket

#functions for sending and receiving messages
def sending():
  msg = input('client:')
  if msg =='bye':
    a=0
  if len(msg)>0:
    s.send(bytes(msg,"utf-8"))
    print('message sent')

def receiving():
  msg = s.recv(1024)
  global a
  if msg =='bye':
    a=0
  if len(msg)>0:
    print(f'server:{msg.decode("utf-8")}')
    
#creating a socket object, by AF_INET we are using IPv4 protocol and by SOCK_STREAM we are using TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host='192.168.0.106'
s.connect((host,1234))                   #establishing connection with a server on 1234

msg = s.recv(1024)
print(f'server:{msg.decode("utf-8")}')

#chatting starts
print("Chatting starts...")
a=0
a=int(input('enter 1 to continue  or 0 to stop:'))        #user opinion 

while a>0:
  sending()
  print('receiving message...')                           #loop for receiving and sending alternatively
  receiving()
print('Disconnecting...')
s.close()                                                #the connection is closed    
    

 
