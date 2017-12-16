import socket
import pickle
import sys
class client ():
   def __init__(self,name):
       print("welcome \n")
       print("you are now connected to server \n")
       while True:
           print("press 1 for adding a new file 2  for searching a file")
           x=input()
           if x=='1':
               s = socket.socket()
               host = socket.gethostname()
               port = 12345
               s.connect((host, port))
               s.send(pickle.dumps("adding_file"))
               s.send(pickle.dumps(str([input('enter file name \n'),name])))
               s.close()
           elif x=='2':
               s = socket.socket()
               host = socket.gethostname()
               port = 12345
               s.connect((host, port))
               s.send(pickle.dumps("searching_files"))
               filename=input('enter file name \n')
               s.send(pickle.dumps(str(filename)))
               print(pickle.loads(s.recv(1024)))
               y=input('wana download y/n \n')
               if y=='y':
                   port_no=input('enter port number \n')
                   C = socket.socket()  # Create a socket object
                   host = socket.gethostname()  # Get local machine name
                   port = port_no # Reserve a port for your service.

                   C.connect((host,int(port)))
                   C.send(pickle.dumps(filename))
                   with open(filename, 'wb') as f:
                       while True:
                           data = C.recv(1024)
                           if not data:
                               break
                           # write data to a file
                           f.write(data)
                   print('file reicivied')
                   f.close()
                   C.close()
                   s.close()
               else:
                    print('thanks for using my program')
                    s.close()


