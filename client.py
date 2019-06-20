# receiving socket

#importing socket module

import socket

port = 1234                                #reserving a port for our service(can try other values also)

s = socket.socket()                        #creating socket object
host = socket.gethostname()                #getting local machine name

s.connect((host,port))
s.send(bytes("Hello server!","utf-8"))

print(f"{s.recv(1024)}[1:]")               #printing the message without b'

received_file = s.recv(1024).decode("utf-8")

with open(f'{received_file}','wb') as f:  #opening the file if existing or just creating a new file if not present
  print('file opened')
  while True:
    print('receiving data ...')
    data = s.recv(1024)                   #getting info in the file from server
    #print(f"data={data}")
    if not data:
      break
    f.write(data)                         #writing the opened file
f.close()
print('Successfully got the file')
s.close()                                 #closing the connection
print('connection closed')
  
