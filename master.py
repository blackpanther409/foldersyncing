
#this is dummy host created to be present at master directory

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()

authorizer.add_user('admin','password','c:/',perm='elramwMT')

authorizer.add_anonymous('c:\\')     

FTPHandler.authorizer = authorizer

FTPServer(('127.0.0.1',21),FTPHandler).serve_forever()
