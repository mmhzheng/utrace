from abc import ABC, abstractmethod
from stream.flowinfo import FlowInfo

class FlowGenerator(ABC):

    @abstractmethod
    def lauch_one_flow(flow : FlowInfo) -> None:
        pass