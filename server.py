import socket
from select import select


class Server:
    ''' Async Socket server using David Beazley algorithm '''
    
    def __init__(self, host: str = '127.0.0.1', port: int = 8000):
        self.host = host
        self.port = port
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.tasks = []
        self.to_read = {}
        self.to_write = {}
    
    def bind_server(self):
        ''' Binding the server and start listening '''
        
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f'[START] Server is now listening port "{self.port}" on host "{self.host}".')
    
    def accept_connection(self):
        ''' Accepting new connections '''
        
        while True:
            yield ('read', self.server_socket)
            client_socket, address = self.server_socket.accept()
            print(f'[CONNECTION] New connection from host "{address[0]}".')
            
            self.tasks.append(self.handle_client(client_socket, address))
    
    def handle_client(self, client_socket: socket.socket, address: tuple):
        ''' Handling client connections '''
        
        while True:
            yield ('read', client_socket)
            request = client_socket.recv(1024)
            print(f'[REQUEST] New request from "{address[0]}".')
            
            if not request:
                print(f'[DISCONNECTION] "{address[0]}" has disconnected.')
                break
            
            yield ('write', client_socket)
            response = 'Response from server.\n'.encode()
            client_socket.send(response)
            
        client_socket.close()
    
    def event_loop(self):
        ''' Async control of event loop '''
        
        while any([self.tasks, self.to_read, self.to_write]):
            while not self.tasks:
                ready_to_read, ready_to_write, _ = select(self.to_read, self.to_write, [])
                
                for sock in ready_to_read:
                    self.tasks.append(self.to_read.pop(sock))

                for sock in ready_to_write:
                    self.tasks.append(self.to_write.pop(sock))
            
            try:
                task = self.tasks.pop(0)
                
                reason, sock = next(task)
                
                if reason == 'read':
                    self.to_read[sock] = task
                    
                if reason == 'write':
                    self.to_write[sock] = task
                
            except StopIteration:
                pass
    
    def run(self):
        ''' Run server '''
        
        try:
            self.bind_server()
            self.tasks.append(self.accept_connection())
            self.event_loop()
            
        except KeyboardInterrupt:
            self.server_socket.close()
        else:
            self.server_socket.close()
            
        finally:
            print('[STOP] Server is stopped.')
        
if __name__ == '__main__':
    server = Server()
    server.run()