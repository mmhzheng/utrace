from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess
import multiprocessing
from typing import List
import random

class RdmaGen(FlowGenerator):
    def __init__(self):
        self.client_processes: List[multiprocessing.Process] = []
        self.server_processes: List[subprocess.Popen] = []

    def setup_servers(self, port_base, number):
        # setup self.number ib_write_bw servers with subprocess model.
        for i in range(number):
            cmd = f"ib_write_bw --disable_pcie_relaxed -p {port_base + i}"
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
        process = multiprocessing.Process(target=self.run_rdma, args=(server_ip, server_port, size, output_file,))
        self.client_processes.append(process)
        process.start()

    def run_rdma(self, server_ip, server_port, size, output_file):
        cmd = f"ib_write_bw -d {server_ip} -p {server_port} -s {size}"
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