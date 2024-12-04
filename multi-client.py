import socket

def Main():
    # Define server address and port
    host = '127.0.0.1'  # Localhost
    port = 12345  # Change to the port your server is listening on

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        s.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        while True:
            # Collect reservation details from the user
            plane_class = input("Enter class (B for Business, E for Economy): ").strip()
            seats = input("Enter number of passengers: ").strip()
            carryon = input("Enter number of carry-ons: ").strip()
            suitcases = input("Enter number of luggages: ").strip()

            # Format the request string
            message = f"{plane_class},{seats},{carryon},{suitcases}"

            # Send the message to the server
            s.send(message.encode('utf-8'))

            # Receive the server's response
            data = s.recv(1024)
            print("Server response:", data.decode('utf-8'))

            # Ask the user if they want to make another reservation
            ans = input("Do you want to continue (y/n): ").strip().lower()
            if ans != 'y':
                print("Closing connection.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        s.close()

if __name__ == "__main__":
    Main()
