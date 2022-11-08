import socket
import threading


''' TODO class Client: ... '''

HOST = '127.0.0.1'
PORT = 8000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

def get_message():
    while True:
        message = client_socket.recv(1024).decode()
        print(message)

def send_message():
    while True:
        message = input().encode()
        client_socket.send(message)


def main():
    threading.Thread(target=get_message).start()
    send_message()
    
if __name__ == '__main__':
    main()