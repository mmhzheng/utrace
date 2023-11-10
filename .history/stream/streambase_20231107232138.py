from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    @abstractmethod
    def another_abstract_method(self, parameter):
        pass

    def my_concrete_method(self):
        print("This is a concrete method.")