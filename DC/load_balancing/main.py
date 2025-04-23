import time

class Server:
    def __init__(self, name):
        self.name = name

    def handle_request(self, request):
        print(f"Server {self.name} is handling request: {request}")
        time.sleep(0.1)  # Simulate processing delay

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

    def distribute_request(self, request):
        server = self.get_next_server()
        server.handle_request(request)

# Simulate 3 servers
servers = [Server(f"S{i}") for i in range(1, 4)]
lb = LoadBalancer(servers)

# Simulate 10 client requests
for i in range(1, 11):
    request = f"Request-{i}"
    lb.distribute_request(request)
