from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
class MySubclass(FlowGenerator):

    def lauch_one_flow(flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
              
        pass