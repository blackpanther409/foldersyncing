#server socket this program(server.py) needs to be run prior to client socket program(client.py)
#socket module is used which comes with python packages by default

import socket

import spacy
import json
nlp = spacy.load("en_core_web_sm")
info={}
#timeout for waiting more than 30 sec with no connection established. You can vary it as you wish, like 2 min(120 sec)...
socket.setdefaulttimeout(30)

#functions for sending and receiving messages also handling errors related to json_file handling
#error handling
def handle():
  with open('chat.txt', 'w') as json_file:
        info = {"sahithi":{"count":1,"POS":"NOUN"}}
        json.dump(info, json_file)
  with open('chat.txt') as json_file:
        info=json.load(json_file)
#sending         
def sending():
  msg = input('server:')
  global a
  if 'bye' in msg.lower().strip():
    a=0
  if len(msg)>0:
    client.send(bytes(msg,"utf-8"))
    print('message sent')
#receiving and saving data of client chat into chat.txt
def receiving():
  msg = client.recv(1024)
  msg = msg.decode("utf-8")
  global a
  if 'bye' in msg.lower().strip():
    a=0
  if len(msg)>0:
    print(f'client:{msg}')

    global info
    msg=nlp(msg)
    try:
      with open('chat.txt') as json_file:
        info=json.load(json_file)
    except json.decoder.JSONDecodeError:
      handle()
    except FileNotFoundError:
      handle()
    #writing
    with open('chat.txt', 'w') as json_file:
      #print("WORD"+' '*9+"COUNT"+' '*3+"POS")
      for i in msg:                             
        if i.text.lower() not in info:
          info[i.text.lower()]={"count":1,"POS":i.pos_}
        else:
          info[i.text.lower()]["count"]=info[i.text.lower()]["count"]+1
        #print(f"{i.text:10}    {info[i.text.lower()]['count']}     {i.pos_}")
      json.dump(info, json_file)     


#creating a socket object, by AF_INET we are using IPv4 protocol and by SOCK_STREAM we are using TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#We can change PORT number but make sure to have same port number in server and client programs
PORT = 1234
#binding hostname with port number and enabling listen 
'''
s.bind((socket.gethostname(),1234)) OR  s.bind(('',1234))
also works instead of s.bind(('0.0.0.0',1234)) but for running server in
windows you should go with s.bind(('0.0.0.0',1234)) others don't work
I recommend going through the following link for more clarity
"https://superuser.com/questions/949428/whats-the-difference-between-127-0-0-1-and-0-0-0-0"
'''
s.bind(('0.0.0.0',PORT))

i=1
while i==1:
    print(f'listening on IP = {socket.gethostname()} PORT = {PORT}')
    s.listen()                                                      #listening for any client online
    print('waiting to establish connection...')
    
    try:
      client, address = s.accept()                                  #getting client details if found any, by establishing the connection
      print(f"Connection from {address} has been established!!!")   #printing the details
      client.send(bytes("Welcome to the server!!","utf-8"))         #sending a message which is coded into bytes

      #chatting starts
      print('Chatting starts...')
      a=0
      a=int(input('Press 1 to accept the connection(any other key to reject):'))            #user opinion 

      while a==1:                                                    #loop for sending  and receivingalternatively
        print('receiving message...')
        receiving()                                                  #receiving message
        if a!=1:
          break
        sending()                                                    #sending message
      print(f'User:{address[0]} disconnected from the chat')
      client.close()                                                 #the connection is closed
      i=int(input('Enter 1 to stay online:'))
    except socket.timeout as error:
      print('Sorry the client is not responding...')
      break
print('Closing server..')                                            #closing the server
