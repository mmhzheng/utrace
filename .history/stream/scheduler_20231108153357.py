import time
from tqdm import tqdm
import threading

S_TO_US = 1e6

class FlowScheduler:
    
    def __init__(self, duration_us : float, flows : list, p = 1):
        """
        Start to generate flows.
        """
        self.threads = [threading.Thread(name=str(i), target=self.start) for i in range(p)]
        self.flows = [[] for _ in range(p)]
        self.duration_us = duration_us
        # divide flows among cores.
        for idx, f in enumerate(flows):
            select = idx % p
            self.flows[select].append(f)
    
    def start(self) -> int:
        thread_id = int(threading.current_thread().name)
        with tqdm(total=len(self.flows)) as pbar:
            start_time = time.perf_counter() * S_TO_US
            for f in self.flows[thread_id]:
                elapsed_time = time.perf_counter() - start_time
                expected_time = self.duration_ms * (i+1) / len(self.flows[thread_id])
                remaining_time = expected_time - elapsed_time
                if remaining_time > 0:
                    time.sleep(remaining_time)

