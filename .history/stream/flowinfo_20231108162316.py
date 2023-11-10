from typing import List, Tuple
import numpy as np

class FlowInfo:
    def __init__(self, id: int, type: str, size: int):
        self.id = id
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self) -> str:
        return f"FlowInfo(id={self.id}, type={self.type}, size={self.size})"
    
    
class FlowCollection:
    def __init__(self, type: str, num: int, min_size: int, max_size: int, distribution: str, distribution_params: List[float]):
        self.id = id
        self.type = type
        self.num = num
        self.min_size = min_size
        self.max_size = max_size
        self.distribution = distribution
        self.distribution_params = distribution_params
        self.flows = []
        self.s = 
        self.generate_flows()
        
    # @output: the number of added flows
    def generate_flows(self) -> None:
        for i in range(self.num):
            size = self.get_flow_size()
            flow = FlowInfo(i, self.type, size)
            self.flows.append(flow)
    
    
    def get_flow_size(self) -> list:
        if self.distribution == 'zipf':
            return (np.random.zipf(self.distribution_params[0], self.num) - 1) 
                        % (self.max_size - self.min_size + 1) + self.min_size 
        elif self.distribution == 'uniform':
            pass
        else:
            raise ValueError(f"Unsupported distribution: {self.distribution}")
        return len(self.flows)
    
