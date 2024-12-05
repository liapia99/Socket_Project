import socket
from threading import Thread, Lock


class_B = 30  # Business class seat limit
class_E = 120  # Economy class seat limit
lock = Lock()  

# function for handling reservations - changed logic to be simpler ---------------------------------------------------------------------
def handle_reservation(plane_class, seat_num, carry_on, luggage, class_B, class_E, lock):
    def reserve_seat(class_type, seat_limit, seat_price):
        if seat_limit < seat_num:
            return class_B, class_E, f"Not enough seats available in {class_type} class."
        if carry_on > seat_num or luggage > (seat_num * 2):
            return class_B, class_E, "Baggage policy violated: 1 carry-on and up to 2 luggages per person."
            
        # update seat count
        seat_limit -= seat_num
        
        # calculate costs
        cost = seat_num * seat_price
        extracost = carry_on * 20 + luggage * 50
        totalcost = cost + extracost
        return class_B, class_E, f"Reserved {seat_num} seats in {class_type} class for ${totalcost}. Remaining: {seat_limit} seats."

    with lock:
        if plane_class.strip().lower() == 'b':
            updated_B, class_E, message = reserve_seat("Business", class_B, 200)
            return updated_B, class_E, message
        elif plane_class.strip().lower() == 'e':
            class_B, updated_E, message = reserve_seat("Economy", class_E, 80)
            return class_B, updated_E, message
        else:
            return class_B, class_E, "Invalid class: Use 'B' for Business or 'E' for Economy."

# multithreaded -----------------------------------------------------------------
# client handling function ----------------------------------------------------------------
def client_handler(conn, addr):
    print(f"[+] Connected to {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break  # client will disconnect

            request = data.decode("utf-8").strip().split(",")
            if len(request) == 4:
                plane_class, seat_num, carry_on, luggage = request
                try:
                    seat_num = int(seat_num)
                    carry_on = int(carry_on)
                    luggage = int(luggage)
                    response = handle_reservation(plane_class.strip(), seat_num, carry_on, luggage)
                except ValueError:
                    response = "Invalid input: seat, carry-on, and luggage must be integers."
            else:
                response = "Invalid request format. Use: 'Class,Seats,CarryOn,Luggage'"

            conn.send(response.encode("utf-8"))
    except Exception as e:
        print(f"Error with client {addr}: {e}")
    finally:
        conn.close()

# main server --------------------------------------------------------------------------------
def main():
    host = "0.0.0.0"
    port = 12202

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)

    print(f"Server listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        Thread(target=client_handler, args=(conn, addr)).start()

if __name__ == "__main__":
    main()
