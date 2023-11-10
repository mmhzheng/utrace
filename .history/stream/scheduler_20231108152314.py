import time
from tqdm import tqdm
import threading


class FlowScheduler:
    
    def __init__(self, flows, p = 1):
        """
        Start to generate flows.
        """
        self.threads = [threading.Thread(name=str(i), target=self.start) for i in range(p)]
        self.flows = [[] for _ in range(p)]
        # divide flows among cores.
        while len(flows) > 0:
            
    
    def start(self) -> int:
        with tqdm(total=len(self.flows)) as pbar:
            for id, flow in enumerate(self.flows[]):
                elapsed_time = time.time() - start_time
                expected_time = total_time * (i+1) / total_actions
                remaining_time = expected_time - elapsed_time
                if remaining_time > 0:
                    time.sleep(remaining_time)
                # 更新进度条
                pbar.update(1)

