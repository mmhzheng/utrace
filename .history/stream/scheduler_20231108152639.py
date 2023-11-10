import time
from tqdm import tqdm
import threading


class FlowScheduler:
    
    def __init__(self, duration, flows, p = 1):
        """
        Start to generate flows.
        """
        self.threads = [threading.Thread(name=str(i), target=self.start) for i in range(p)]
        self.flows = [[] for _ in range(p)]
        self.duration = duration
        # divide flows among cores.
        for idx, f in enumerate(flows):
            select = idx % p
            self.flows[select].append(f)
    
    def start(self) -> int:
        thread_id = int(threading.current_thread().name)
        with tqdm(total=len(self.flows)) as pbar:
            start_time = time.time()
            for id, flow in enumerate(self.flows[thread_id]):
                elapsed_time = time.time() - start_time
                expected_time = total_time * (i+1) / total_actions
                remaining_time = expected_time - elapsed_time
                if remaining_time > 0:
                    time.sleep(remaining_time)
                # 更新进度条
                pbar.update(1)

