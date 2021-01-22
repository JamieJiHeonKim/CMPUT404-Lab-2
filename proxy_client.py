import socket, time, sys

host = "www.google.com"
port = 80
BUFFER_SIZE = 1024


payload=f"GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(address):
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(address)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)
        full_data = s.recv(BUFFER_SIZE)
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect(('127.0.0.1', 8001))

if __name__ == "__main__":
    main()

