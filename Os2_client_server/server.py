import threading
import socket
import pickle
class my_server (threading.Thread):
   s = socket.socket()
   name=0
   def __init__(self):
        threading.Thread.__init__(self)  # Create a socket object
        self.s.bind(('', 0))  # Bind to the port
        self.s.listen(5)  # Now wait for client connection.
        self.name = self.s.getsockname()[1]
   def run(self):
       while True:
           c, addr = self.s.accept()
           print('Got connection from', addr)
           c.send('Thank you for connecting')
           c.close()