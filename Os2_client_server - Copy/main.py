from client import client
from server import my_server
s=my_server()
s.start()
c=client(s.name)