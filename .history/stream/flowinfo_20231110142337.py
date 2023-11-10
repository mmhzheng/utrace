from typing import List, Tuple
import numpy as np
import logging

class FlowInfo:
    def __init__(self, id: int, client : str, server_ip : str, server_port : str, type: str, size: int):
        self.id = id
        self.client = client
        self.server_ip = server_ip
        self.server_port = server_port
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self) -> str:
        return f"Flow {self.id} from {self.client} to {self.server_ip}:{self.server_port} with size {self.size} bytes"
    
    
class FlowCollection:
    def __init__(self, client : str, server_ip : str, server_port : str, type: str, num: int, 
                 min_size: int, max_size: int, distribution: str, distribution_params: List[float]):
        self.client = client
        self.server_ip = server_ip
        self.server_port = server_port
        self.type = type
        self.num = num
        self.min_size = min_size
        self.max_size = max_size
        self.distribution = distribution
        self.distribution_params = distribution_params
        self.flows = []
        self.s = self.get_flow_size()
        self.generate_flows()
        
    def get_flows(self) -> List[FlowInfo]:
        return self.flows
    
    # @output: the number of added flows
    def generate_flows(self) -> None:
        for i in range(self.num):
            flow = FlowInfo(i, self.client, self.server_ip, self.server_port, self.type, self.s[i])
            logging.info(f"Generate flow: {str(flow)}")
            self.flows.append(flow)
    
    def get_flow_size(self) -> list:
        if self.distribution == 'zipf':
            return (np.random.zipf(self.distribution_params[0], self.num) - 1) % (self.max_size - self.min_size + 1) + self.min_size 
        elif self.distribution == 'uniform':
            return np.random.uniform(self.min_size, self.max_size, self.num)
        elif self.distribution == 'FacebookHadoop':
            
        else:
            raise ValueError(f"Unsupported distribution: {self.distribution}")
    
    def print_flows(self) -> None:
        for flow in self.flows:
            print(str(flow))
