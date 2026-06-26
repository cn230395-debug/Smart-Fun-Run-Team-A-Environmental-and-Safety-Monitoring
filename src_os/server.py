import socket
import threading
from database_handler import save_to_excel, initialize_excel

HOST = '0.0.0.0'
PORT = 8080

lock = threading.Lock()

initialize_excel()

def handle_client(conn, addr):
    print(f"Connected: {addr}")

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        try:
            temperature, humidity = map(float, data.split(","))

            with lock:  # Mutex synchronization
                save_to_excel(temperature, humidity)

            print(f"Temp: {temperature}°C | Humidity: {humidity}%")

        except:
            print("Invalid data received")

    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Server running on port {PORT}")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )
    thread.start()
