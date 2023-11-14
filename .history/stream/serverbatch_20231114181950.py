
from typing import List

class ServerBatch:
    
    def __init__(self, port_base, number):
        self.port_base = port_base
        self.number = number
        self.servers = List()
        
    def setup_servers(self):
        # setup self.number iperf servers with subprocess model.
        for i in range(self.number):
            cmd = f"iperf -s -p {self.port_base + i} -Z dctcp"
            self.servers.append(server)
