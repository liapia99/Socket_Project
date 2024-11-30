# Socket_Project

An airplane has 30 business class seats and 120 economy class seats. Business class costs $200 a seat
and economy costs $80 a seat for a flight from New York to Boston. The charge for a carry-on is $20
and luggage is $50 a piece with a max of two bags.
Write a server/client program to sell the tickets.

The client prompt the user to enter the required class, the number of people in the group, how
many carry-ons they have (should not exceed group size), and how many luggage (should not
exceed twice group size). The program then contacts the server to book the seats (if possible), and
then if the client gets an OK from the server, it print out a receipt. An order will be refused if there
are not enough seats in the required area. The server reports the remaining seats in both business
and economy before and after each transaction. The server shuts down when ALL tickets are sold.
Note: You need to have a protocol of the conversation between the client and the server.

Sample interactions :
Client: Business or economy: B
Client: Number of passengers? 2
Client: Number of carry-ons? 2
Client: Number of luggage? 3
Server: Great, You got 2 tickets for $590
Server: Remaining seats: Business 28 Economy 120
Client: Business or economy: E
Client: Number of passengers? 5
Client: Number of carry-ons? 4
Client: Number of luggage? 2
Server: Great, You got 5 tickets for $580
Server: Remaining seats: Business 28 Economy 115

Extra credit:
- Create a “Multithreaded” server so it can deal with multiple clients simultaneously.
- Make a nice graphical interface, so the user can pick seats.
