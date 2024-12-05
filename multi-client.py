import socket

def main():
    # server address and port
    host = '127.0.0.1'  
    port = 12202

    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to the server
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            # collect reservation details from the user
            plane_class = input("Enter class (B for Business, E for Economy): ").strip()
            seats = input("Enter number of passengers: ").strip()
            carryon = input("Enter number of carry-ons: ").strip()
            suitcases = input("Enter number of luggage: ").strip()

            # format the string
            message = f"{plane_class},{seats},{carryon},{suitcases}"

            # send the message to the server
            s.send(message.encode('utf-8'))

            # receive the server's response
            data = s.recv(1024)
            print("Server response:", data.decode('utf-8'))

            # ask user if they want to make another reservation
            ans = input("Do you want to continue (y/n): ").strip().lower()
            if ans != 'y':
                print("Closing connection.")
                break
        s.close()

if __name__ == "__main__":
    main()
