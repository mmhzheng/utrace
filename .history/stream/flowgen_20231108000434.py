from abc import ABC, abstractmethod

class FlowGenerator(ABC):
    
    def __init__(self, flows : list):
        """
        Define 
        """
        self.flows = flows
        self.terminate = False
    
    def start(self):
        while
        self.lauch_one_flow()    
    
    @abstractmethod
    def lauch_one_flow(self):
        pass

    def my_concrete_method(self):
        print("This is a concrete method.")