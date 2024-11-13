#   TCPClient.py                                     
 

from socket import *

serverName = "148.166.146.230"

serverPort = 12001

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

 
plane_class = input("Business or Economy: ")
clientSocket.send(bytes(plane_class, "utf-8"))

seats = input("Number of seats ")
clientSocket.send(bytes(plane_class, "utf-8"))

#print ("Sent to Square Server: ", sentence)
modified_plane_class = clientSocket.recv(1025)
print (int(modified_plane_class))
      
clientSocket.close()
