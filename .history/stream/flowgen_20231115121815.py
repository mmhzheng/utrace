from abc import ABC, abstractmethod
from stream.flowinfo import FlowInfo

class FlowGenerator(ABC):

    @abstractmethod
    def setup_servers(self, port_base, number):
        pass
      
            
    @abstractmethod
    def lauch_one_flow(flow : FlowInfo) -> None:
        pass