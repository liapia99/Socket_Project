from socket import *

serverName = ""

serverPort = 12009

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, serverPort))





plane_class = input("Enter class (B for Business, E for Economy): ").strip()
clientSocket.send(plane_class.encode("utf-8"))

seats = input("Enter number of passengers: ").strip()
clientSocket.send(seats.encode("utf-8"))  

carryon = input("Enter number of carry-ons: ").strip()
clientSocket.send(carryon.encode("utf-8")) 

suitcases = input("Enter number of luggages: ").strip()
clientSocket.send(suitcases.encode("utf-8")) 

response = clientSocket.recv(1024).decode("utf-8")
print("Receipt:", response)

# Close the connection
clientSocket.close()
