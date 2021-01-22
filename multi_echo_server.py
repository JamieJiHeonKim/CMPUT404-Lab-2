import socket, time, sys

from multiprocessing import Process

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        start.bind((HOST, PORT))
        start.listen(2)
        
        while True:
            conn, addr = start.accept()
            process = Process(target=handle_echo, args=(addr, conn))
            process.daemon = True
            process.start()
            print("Process is starting", process)

def handle_echo(addr, conn):
    print("Connection with", addr)
    full_data = conn.recv(BUFFER_SIZE)
    conn.sendall(full_data)
    conn.shutdown(socket.SHUT_RDWR)
    conn.close()

if __name__ == "__main__":
    main()
