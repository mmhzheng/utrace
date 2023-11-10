from abc import ABC, abstractmethod

class FlowGenerator(ABC):
    
    def __init__(self, flows : list):
        """
        Define 
        """
        self.flows = flows
        self.terminate = False
    
    def start(self):
        while not self.terminate:
            self.lauch_one_flow()  
    
    @abstractmethod
    def lauch_one_flow(self):
        pass