from abc import ABC, abstractmethod

class FlowGenerator(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    def my_concrete_method(self):
        print("This is a concrete method.")