from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo, FlowCollection
import subprocess
import multiprocessing
from typing import List
import random

class RdmaGen(FlowGenerator):
    def __init__(self, fc : FlowCollection):
        self.client_processes: List[multiprocessing.Process] = []
        self.server_processes: List[subprocess.Popen] = []

    def setup_servers(self, fc : FlowCollection) -> None:
        # setup self.number ib_write_bw servers with subprocess model.
        for f in range(fc.flows):
            cmd = f"ib_write_bw --disable_pcie_relaxed -d {fc.server_nic} -p {f.server_port} -s {f.size // 5}  -n 5"
            server = subprocess.Popen(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.server_processes.append(server)

    def teardown_servers(self) -> None:
        for server in self.server_processes:
            server.kill()

    def lauch_one_flow(self, flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        server_ip = flow.server_ip
        server_port = flow.server_port
        output_file = f"log/rdma_output_flow{id}.txt"
        process = multiprocessing.Process(target=self.run_rdma, args=(flow, output_file,))
        self.client_processes.append(process)
        process.start()

    def run_rdma(self, flow : FlowInfo, output_file : str):
        cmd = f"ib_write_bw --disable_pcie_relaxed -d {} 172.16.200.10 -p 50001  -s 100000  -n 5"
        print(f"rdma flow {server_ip}:{server_port} started, size: {size} bytes")
        if random.random() < 0.05:
            with open(output_file, 'w') as file:
            # sample some flow to record log
               subprocess.run(cmd.split(), stdout=file, stderr=subprocess.PIPE)
        else:
            subprocess.run(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def wait_for_all(self):
        for process in self.client_processes:
                process.join()