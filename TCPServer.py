from socket import *

# has to be the same port as the client!
serverPort = 12009

# create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))

# server begins listening for incoming TCP requests
serverSocket.listen(1)


class_B = 30  # Limit of Business class seats
class_E = 120  # Limit of Economy class seats

carry_on = 0
luggage = 0

cost = 0

extracost = 0
totalcost = 0 

print("The Socket Project running over TCP is ready to receive...")


while 1:
    # server waits for incoming requests; new socket created on return
    connectionSocket, addr = serverSocket.accept()
     
    # read a sentence of bytes from socket sent by the client
    connectionSocket, addr = serverSocket.accept# Receive and process data from client
    
    plane_class = connectionSocket.recv(1024).decode("utf-8").strip()
    seats = connectionSocket.recv(1024).decode("utf-8").strip()
    carryon = connectionSocket.recv(1024).decode("utf-8").strip()
    suitcases = connectionSocket.recv(1024).decode("utf-8").strip()

    seat_num = int(seats)
    carry_on = int(carryon)
    luggage = int(suitcases)
    
# Reservation logic

# Business class
    if plane_class == 'B':
        # check if there are seats left in business
        if class_B == 0:
            response = "No seats left in Business class."
        # if there are enough seats (greater than or equal to)
        elif class_B >= seat_num:
            class_B -= seat_num #if there are enough seats, subtract the taken seats from the available seating
            # check the carry-ons and luggages ( if they meet the requirements )
            if carry_on == seat_num and luggage <= (seat_num * 2):
                # calculate cost of seat only 
                cost = seat_num * 200
                # calculate cost of luggage and carry-on only 
                extracost = (carry_on * 20) + (luggage * 50)

                totalcost = cost + extracost
                response = (f"Great, You got {seat_num} for ${totalcost}."
                            f"Remaining seats: Economy {class_E} Business {class_B}")
            else:
                response = "Baggage policy violated: 1 carry-on per person, up to 2 luggages per person."
        else:
            response = "Not enough seats available in Business class."
# Economy class -----------------------------------------------------------------------------------------------
    elif plane_class == 'E':
        # check if there are seats left in economy
        if class_E == 0:
            response = "No seats left in Economy class."
            # if there are enough seats (greater than or equal to)
        elif class_E >= seat_num:
            class_E -= seat_num
            if carry_on == seat_num and luggage <= (seat_num * 2):
                # calculate cost of seat only 
                cost = seat_num * 80
                # calculate cost of luggage and carry-on only 
                extracost = (carry_on * 20) + (luggage * 50)

                totalcost = cost + extracost
                response = (f"Great, You got {seat_num} for ${totalcost}."
                            f"Remaining seats: Economy {class_E} Business {class_B}")
            else:
                response = "Baggage policy violated: 1 carry-on per person, up to 2 luggages per person."
        else:
            response = "Not enough seats available in Economy class."
    else:
        response = "Wrong value given. Use 'B' for Business or 'E' for Economy."



    # output to console the sentence sent back to the client 
    connectionSocket.send(response.encode("utf-8"))

    # close the TCP connection; the welcoming socket continues
    connectionSocket.close()
