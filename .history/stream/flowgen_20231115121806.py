from abc import ABC, abstractmethod
from stream.flowinfo import FlowInfo

class FlowGenerator(ABC):


    def setup_servers(self, port_base, number):
        # setup self.number iperf servers with subprocess model.
        for i in range(number):
            cmd = f"iperf -s -p {port_base + i} -Z dctcp"
            server = subprocess.Popen(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.server_processes.append(server)
            
    @abstractmethod
    def lauch_one_flow(flow : FlowInfo) -> None:
        pass