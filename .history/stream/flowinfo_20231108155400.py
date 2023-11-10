from typing import List, Tuple
# generate a flow info class

class FlowInfo:
    
    def __init__(self, id, type, size):
        self.id = id
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self):
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
        self.generate_flows()
        
    def generate_flows(self) -> None:
        for i in range(self.num):
            size = self.get_flow_size()
            flow = FlowInfo(i, self.type, size)
            self.flows.append(flow)
            
    def get_flow_size(self) -> int:
        # TODO: implement flow size generation based on distribution
        return self.min_size
    
class FlowInfo:
    
    def __init__(self, id: int, type: str, size: int):
        self.id = id
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self) -> str:
        return f"FlowInfo(id={self.id}, type={self.type}, size={self.size})"
        self.generate_flows()
    