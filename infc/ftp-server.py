from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer()
authorizer.add_user("iwm1", "iwm1@password", "/home/mikku", perm="elradfmw")
authorizer.add_anonymous("/home/mikku", perm="elradfmw")

handler = FTPHandler
handler.authorizer = authorizer

server = FTPServer(("52.172.135.86", 21), handler)
server.serve_forever()