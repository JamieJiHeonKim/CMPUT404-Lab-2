import socket, time, sys

HOST = ""
PORT = 8001
BUFFER_SIZE = 1024

#get host information
def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print ('Hostname could not be resolved. Exiting')
        sys.exit()

    print (f'Ip address of {host} is {remote_ip}')
    return remote_ip


def main():
    host = "www.google.com"
    port = 80

    # connect to google
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as start:
        start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        start.bind((HOST, PORT))
        start.listen(1)

        # while sending the data into smaller size
        while True:
            conn, addr = start.accept()
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as end:

                remote_ip = get_remote_ip(host)
                end.connect((remote_ip, port))

                send_full_data = conn.recv(BUFFER_SIZE)
                end.sendall(send_full_data)
                end.shutdown(socket.SHUT_WR)

                data = end.recv(BUFFER_SIZE)
                print(f"Sending recieved data {data} to client")
                conn.send(data)
            conn.close()

if __name__ == "__main__":
    main()

