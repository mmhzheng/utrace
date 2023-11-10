from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess
import logging

class IperfGen(FlowGenerator):
    def __init__(self, server_ip : str, server_port : int):
        self.tasks = []
        self.server_ip = server_ip
        self.server_port = server_port

    def lauch_one_flow(self, flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        logging.debug(f"Iperf flow {id} with size {size} bytes start")
        
 