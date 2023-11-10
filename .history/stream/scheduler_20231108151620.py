import time
from tqdm import tqdm
import threading


class FlowScheduler:
    
    def __init__(self, flows, p = 1):
        """
        Start to generate flows.
        """
        self.threads = [threading.Thread(id = i, target=self.start) for i in range()]
        self.flows = [[] for _ in range()]
        
        for idx, f in enumerate(flows):
            if idx % p == 0:
        


    def start(self) -> int:
        with tqdm(total=len(self.flows)) as pbar:
            for id, flow in enumerate(self.flows):
                elapsed_time = time.time() - start_time
                expected_time = total_time * (i+1) / total_actions
                remaining_time = expected_time - elapsed_time
                if remaining_time > 0:
                    time.sleep(remaining_time)
                # 更新进度条
                pbar.update(1)

