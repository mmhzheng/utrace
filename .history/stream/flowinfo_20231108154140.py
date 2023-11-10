# generate a flow info class

class FlowInfo:
    
    def __init__(self, id, type, size):
        self.id = id
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self):
        return f"FlowInfo(id={self.id}, type={self.type}, size={self.size})"


class FlowCollection:
    
    