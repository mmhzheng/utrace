# generate a flow info class

class FlowInfo:
    
    def __init__(self, type, size):
        self.size = size
        self.type = type
        
    def __str__(self):
        return f"FlowInfo(type={self.type}, size={self.size})"
    
    