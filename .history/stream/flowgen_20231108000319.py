from abc import ABC, abstractmethod

class FlowGenerator(ABC):
    
    def __init__(self, flows):
        """
        Define 
        """
    
    @abstractmethod
    def my_abstract_method(self):
        pass

    def my_concrete_method(self):
        print("This is a concrete method.")