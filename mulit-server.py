import socket
from threading import Thread, Lock


class_B = 30  # Business class seat limit
class_E = 120  # Economy class seat limit
lock = Lock()  

def handle_reservation(plane_class, seat_num, carry_on, luggage):
    global class_B, class_E

    with lock:  
        if plane_class == "B":
            if class_B < seat_num:
                return "Not enough seats available in Business class."
            if carry_on > seat_num or luggage > (seat_num * 2):
                return "Baggage policy violated: 1 carry-on and up to 2 luggages per person."
            class_B -= seat_num
            cost = seat_num * 200
            extracost = carry_on * 20 + luggage * 50
            totalcost = cost + extracost
            return f"Reserved {seat_num} seats in Business class for ${totalcost}. Remaining: {class_B} seats."
        elif plane_class == "E":
            if class_E < seat_num:
                return "Not enough seats available in Economy class."
            if carry_on > seat_num or luggage > (seat_num * 2):
                return "Baggage policy violated: 1 carry-on and up to 2 luggages per person."
            class_E -= seat_num
            cost = seat_num * 80
            extracost = carry_on * 20 + luggage * 50
            totalcost = cost + extracost
            return f"Reserved {seat_num} seats in Economy class for ${totalcost}. Remaining: {class_E} seats."
        return "Invalid class: Use 'B' for Business or 'E' for Economy."

# multithreaded client thread
class ClientThread(Thread):
    def __init__(self, conn, ip, port):
        Thread.__init__(self)
        self.conn = conn
        self.ip = ip
        self.port = port
        print(f"[+] New connection from {ip}:{port}")

    def run(self):
        try:
            while True:
                data = self.conn.recv(1024)
                if not data:
                    print(f"[-] Connection closed by {self.ip}:{self.port}")
                    break

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

                self.conn.sendall(response.encode("utf-8"))
        except Exception as e:
            print(f"Error with client {self.ip}:{self.port}: {e}")
        finally:
            self.conn.close()

def main():
    TCP_IP = '0.0.0.0'
    TCP_PORT = 2004

    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcpServer.bind((TCP_IP, TCP_PORT))
    tcpServer.listen(5)
    threads = []

    print(f"Server listening on {TCP_IP}:{TCP_PORT}")

    try:
        while True:
            conn, (ip, port) = tcpServer.accept()
            new_thread = ClientThread(conn, ip, port)
            new_thread.start()
            threads.append(new_thread)
    except KeyboardInterrupt:
        print("Server shutting down.")
    finally:
        for thread in threads:
            thread.join()
        tcpServer.close()

if __name__ == "__main__":
    main()
