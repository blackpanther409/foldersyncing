#client socket

import socket

#functions for sending and receiving messages
def sending():
  msg = input('client:')
  global a
  if msg.lower().strip() =='bye':
    a=0
  if len(msg)>0:
    s.send(bytes(msg,"utf-8"))
    print('message sent')

def receiving():
  msg = s.recv(1024)
  msg = msg.decode("utf-8")
  global a
  if msg.lower().strip()=='bye':
    a=0
  if len(msg)>0:
    print(f'server:{msg}')
    
#creating a socket object, by AF_INET we are using IPv4 protocol and by SOCK_STREAM we are using TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#host='192.168.0.106'
host=socket.gethostname()


s.connect((host,1234))                   #establishing connection with a server on 1234

msg = s.recv(1024)
print(f'server:{msg.decode("utf-8")}')

#chatting starts
print("Chatting starts...")
a=0
a=int(input('Press 1 to accept the connection(any other key to reject)'))        #user opinion 

while a==1:
  sending()
  if a!=1:
    break
  print('receiving message...')                           #loop for receiving and sending alternatively
  receiving()
print(f'User:{host} disconected from the chat')
s.close()                                                #the connection is closed    



 
