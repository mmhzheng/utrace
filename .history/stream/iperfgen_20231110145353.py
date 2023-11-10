from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess
import multiprocessing
from typing import List
import logging

class IperfGen(FlowGenerator):
    def __init__(self):
        self.processes: List[multiprocessing.Process] = []

    def lauch_one_flow(self, flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        output_file = f"iperf_output_flow{id}.txt"

        logging.debug(f"Iperf flow {id} with size {size} bytes start")

        process = multiprocessing.Process(target=self.run_iperf, args=(output_file,))
        process.start()

        self.processes.append(process)

    def run_iperf(self, server_ip, server_port, output_file):
        cmd = f"iperf -c {server_ip} -p {server_port} -Z dctcp"
        with open(output_file, 'w') as file:
            subprocess.run(cmd.split(), stdout=file, stderr=subprocess.PIPE)

    def wait_for_all(self):
        for process in self.processes:
            process.join()
