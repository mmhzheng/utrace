from typing import List, Tuple
import numpy as np
import logging
from scipy.interpolate import interp1d
import random

class FlowInfo:
    def __init__(self, id: int, client : str, server_ip : str, server_port : str, type: str, size: int):
        self.id = id
        self.client = client
        self.server_ip = server_ip
        self.server_port = server_port
        self.type = type # tcp or rdma
        self.size = size
        
    def __str__(self) -> str:
        return f"Flow {self.id} from {self.client} to {self.server_ip}:{self.server_port} with size {self.size} bytes"
    
    
class FlowCollection:
    def __init__(self, network: dict, client : str, server_ip : str, server_port : int, 
                 type: str, num: int, distribution: str, distribution_params: List[float]):
        self.network = network
        self.client = client
        self.server_ip = server_ip
        self.server_port = server_port
        self.type = type
        self.num = num
        self.distribution = distribution
        self.distribution_params = distribution_params
        self.flows = []
        self.s = self.get_flow_size()
        self.generate_flows()
        
    def get_flows(self) -> List[FlowInfo]:
        return self.flows
    
    # @output: the number of added flows
    def generate_flows(self) -> None:
        for i in range(self.num):
            flow = FlowInfo(i, self.network[self.client], self.network[self.server_ip], self.server_port, self.type, self.s[i])
            logging.info(f"Generate flow: {str(flow)}")
            self.flows.append(flow)
    
    def get_flow_size(self) -> list:
        if self.distribution == 'zipf':
            min_size = 0
            max_size = 0
            if len(self.distribution_params) == 3:
                min_size = self.distribution_params[1]
                max_size = self.distribution_params[2]
            return (np.random.zipf(self.distribution_params[0], self.num) - 1) % (max_size - min_size + 1) + min_size 
        elif self.distribution == 'uniform':
            return np.random.uniform(self.min_size, self.max_size, self.num)
        elif self.distribution in ['FacebookHadoop', 'AliStorage', 'GoogleRPC', 'WebSearch']:
            filename = 'scripts/cdf/' + self.distribution + '.txt'
            sizes = []
            percentiles = []
            try:
                with open(filename, 'r') as file:
                    for line in file:
                        size, percentile = map(float, line.split())
                        sizes.append(size)
                        percentiles.append(percentile)
            except FileNotFoundError:
                print(f"File {filename} non-exist.")
                return None, None
            except Exception as e:
                print(f"Failure read {filename}: {e}")
                return None, None
            f = interp1d(percentiles, sizes, kind='linear', fill_value="extrapolate")
            random_percentiles = [random.uniform(0, 100) for _ in range(self.num)]
            return [int(size) for size in f(random_percentiles)]
        else:
            raise ValueError(f"Unsupported distribution: {self.distribution}")
        
    def print_flows(self) -> None:
        for flow in self.flows:
            print(str(flow))
