from abc import ABC, abstractmethod
from stream.flow import FlowInfo

class FlowGenerator(ABC):
    def __init__(self, flows : list):
        """
        Define 
        """
        self.flows = flows
        self.terminate = False
    
    def start(self):
        for flow in self.flows:
            self.lauch_flow(flow)  
    
    @abstractmethod
    def lauch_one_flow(flow : FlowInfo) -> None:
        pass