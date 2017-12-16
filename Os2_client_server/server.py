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
             filename = pickle.loads(c.recv(1024))
             f = open(filename, 'rb')
             l = f.read(1024)
             while (l):
                 c.send(l)
                 print('Sent ', repr(l))
                 l = f.read(1024)
             f.close()
             print('Done sending')
             c.close()