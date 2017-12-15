from client import client
from server import my_server
s=my_server()
s.start()
print(s.name)
c=client(s.name)