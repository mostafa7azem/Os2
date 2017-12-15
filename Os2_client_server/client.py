import socket
import pickle
class client ():
   def __init__(self,name):
       s = socket.socket()  # Create a socket object
       host = socket.gethostname()  # Get local machine name
       port = 12345  # Reserve a port for your service.
       print("welcome \n")
       print("you are now connected to server \n")
       print("press 1 for adding a new file 2  for searching a file 3 for exit ")
       x=input()
       if x=='1':
           s.connect((host, port))
           s.send(pickle.dumps("adding_file"))
           s.send(pickle.dumps(str([input('enter file name \n'),name])))
           s.close()
       elif x=='2':
           s.connect((host, port))
           s.send(pickle.dumps("searching_files"))
           s.send(pickle.dumps(str(input('enter file name \n'))))
           s.close()


