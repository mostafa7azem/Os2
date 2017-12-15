#!/usr/bin/python

import threading
import socket
import pickle
import ast
class my_main_server (threading.Thread):
   s = socket.socket()
   dic=[]
   def __init__(self):
        threading.Thread.__init__(self)  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = 12345  # Reserve a port for your service.
        self.s.bind((host, port))  # Bind to the port
        self.s.listen(5)  # Now wait for client connection.

   def run(self):
       while True:
           c, addr = self.s.accept()
           print(bytes('Got connection from', 'utf-8'), addr)
           x=pickle.loads(c.recv(1024))
           if x=="adding_file":
               recived=ast.literal_eval(pickle.loads(c.recv(1024)))
               self.dic.append(recived)
               print(self.dic)
               c.close()
           if x=="searching_files":
               recived = pickle.loads(c.recv(1024))
               search=[]
               for  item in self.dic:
                   if item[0]==recived:
                       search.append(item[1])
               c.send(pickle.dumps(search))
               c.close()

