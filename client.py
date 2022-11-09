import socket
import threading


class Client:
    def __init__(self, host: str = '127.0.0.1', port: int = 8000):  
        self.host = host
        self.port = port
        
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        self.client_socket.connect((self.host, self.port))

    def get_message(self):
        while True:
            message = self.client_socket.recv(1024).decode()
            print(message)

    def send_message(self):
        while True:
            message = input().encode()
            self.client_socket.send(message)

    def event_loop(self):
        threading.Thread(target=self.get_message).start()
        self.send_message()
        
    def run(self):
        self.connect_to_server()
        self.event_loop()
    
if __name__ == '__main__':
    client = Client()
    client.run()