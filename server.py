#sending socket

#importing socket module

import socket

port = 1234                 #reserving a port for our service(can try other values also)

s = socket.socket()         #creating socket object
host = socket.gethostname() #getting local machine name
s.bind((host,port))         #bind to the port
s.listen()                  #Wait for client connection

print("Master is ready to send new files...")

while True:
  client,addr = s.accept()  #establishing connection with client
  print(f'Connection established with {addr}')
  data = client.recv(1024)
  print(f'Server received a message:{repr(data)[1:]}')
  client.send(bytes("Hello client!","utf-8"))
  filename='file.txt' 
  client.send(bytes(filename,"utf-8"))
  f = open(filename,'rb')                       #opening the file given in the filename and sending it to the client socket
  l = f.read(1024)
  while(l):
    client.send(l)
    #print('Sent ',repr(l))
    l = f.read(1024)
  f.close()

  print('Done sending')
  client.send(bytes('Thank you for connecting','utf-8'))
  client.close()
