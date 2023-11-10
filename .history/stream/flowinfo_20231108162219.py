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
        self.s = (np.random.zipf(a, size) - 1) % (max_val - min_val + 1) + min_val

    # 然后，我们通过取模运算将这个分布变换到[0, max_val-min_val]，并加上min_val，得到最终的[min_val, max_val]的分布
    return s 
        self.generate_flows()
        
    # @output: the number of added flows
    def generate_flows(self) -> None:
        for i in range(self.num):
            size = self.get_flow_size()
            flow = FlowInfo(i, self.type, size)
            self.flows.append(flow)
    
    
    def get_flow_size(self) -> int:
        if self.distribution == 'zipf':
            return 
        elif self.distribution == 'uniform':
            pass
        else:
            raise ValueError(f"Unsupported distribution: {self.distribution}")
        return len(self.flows)
    
