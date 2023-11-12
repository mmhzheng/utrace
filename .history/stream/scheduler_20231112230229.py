import time
from tqdm import tqdm
import threading
import logging
from stream.iperfgen import IperfGen
from stream.flowinfo import FlowInfo
from typing import List
S_TO_US = 1e6

class FlowScheduler:
    def __init__(self, duration_s : float, flows: list, p = 1):
        """
        Start to generate flows.
        """
        self.threads = [threading.Thread(name=str(i), target=self.__start) for i in range(p)]
        self.flows = [[] for _ in range(p)]
        self.duration_perf_count = duration_s * S_TO_US
        # divide flows among cores.
        for idx, f in enumerate(flows):
            select = idx % p
            self.flows[select].append(f)
        self.iperfGens = [IperfGen() for _ in range(p)] 
           
    def run(self) -> None:
        for t in self.threads:
            t.start()
        for t in self.threads:
            t.join()
        for iperfGen in self.iperfGens:
            iperfGen.wait_for_all()
        
    def __start(self) -> None:
        thread_id = int(threading.current_thread().name)
        start_time = time.perf_counter() * S_TO_US
        for i, f in enumerate(self.flows[thread_id]):
            ################ Do something
            self.iperfGens[thread_id].lauch_one_flow(f)
            ################
            logging.debug(f"[{time.perf_counter()}] thread {thread_id} fork a flow : {f.id}, {f.size} bytes")
            expected_time_point = start_time + (self.duration_perf_count * (i+1) / len(self.flows[thread_id]))
            while time.perf_counter()* S_TO_US < expected_time_point:
                pass
        pass
        print(f"Thread {thread_id} All flows are generated. Wait for all flows to finish.")
        