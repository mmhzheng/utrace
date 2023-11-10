from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess
import multiprocessing
from typing import List
import logging

class IperfGen(FlowGenerator):
    def __init__(self, server_ip : str, server_port : int):
        self.processes: List[multiprocessing.Process] = []
        self.server_ip = server_ip
        self.server_port = server_port

    def lauch_one_flow(self, flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        output_file = f"iperf_output_{id}.txt"

        logging.debug(f"Iperf flow {id} with size {size} bytes start")

        process = multiprocessing.Process(target=self.run_iperf, args=(output_file,))
        process.start()

        self.processes.append(process)
        
        
