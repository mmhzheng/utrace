from abc import abstractmethod
from stream.flowgen import FlowGenerator

class MySubclass(FlowGenerator):
    
    @abstractmethod
    def lauch_one_flow(flow):
        pass