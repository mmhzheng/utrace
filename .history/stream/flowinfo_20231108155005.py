# generate a flow info class

class FlowInfo:
    
    def __init__(self, id, type, size):
        self.id = id
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self):
        return f"FlowInfo(id={self.id}, type={self.type}, size={self.size})"


class FlowCollection:
    # type: tcp
    # num: 100
    # min_size : 64
    # max_size : 102400
    # distribution: zipf
    # distribution_params: [1.5]
    def __init__(self, type, num, min_size, max_size, distribution, distribution_params):
        self.ty
        
    