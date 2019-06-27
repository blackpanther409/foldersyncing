'''
This program helps you view all the words collected (from the chat of the server)
by the server program into the text file called chat.txt 
'''
#spacy need to be installed
#jason is a default module
import spacy
import json

nlp = spacy.load("en_core_web_sm")

#Reading and printing the words,count and parts of speech(POS)
try:
  with open('chat.txt') as json_file:
      info=json.load(json_file)
      print("The words collected are:")
      print("WORD"+' '*14+"COUNT"+' '*2+"POS")
      for i in info:
        print(f"{i:20}{str(info[i]['count']):5}{info[i]['POS']}")
#Throwing error message incase the file has nothing
except json.decoder.JSONDecodeError:    
  print("Sorry no words recorded yet to display!")
except FileNotFoundError:
  print("It seems server and client didn't chat atleast once!")
