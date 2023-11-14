
from typing import List

class ServerBatch:
    
    def __init__(self, port_base, number):
        self.port_base = port_base
        self.number = number
        self.servers = List()
        
    def setup_servers(self):
        # setup self.number iperf servers with subprocess model.
        for i in range(self.number):
            server = IperfServer(self.port_base + i)
            server.start()
            self.servers.append(server)
