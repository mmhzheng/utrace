from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess
import logging

class IperfClient(FlowGenerator):
    def __init__(self):
        self.tasks = []

    def lauch_one_flow(flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        
        
 