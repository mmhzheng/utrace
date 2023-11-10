import time
from tqdm import tqdm


class FlowScheduler:
    
    def __init__(self, flows):
        """
        Start to generate flows.
        """
        self.flows = flows


    def start(self) -> int:
        with tqdm(total=len(self.flows)) as pbar:
            for id, flow in enumerate(self.flows):
                # 执行某个动作
                # ...

                # 模拟动作耗时
                time.sleep(0.001)

                # 更新进度条
                pbar.update(1)


def dynamic_execution(total_actions, total_time):
    
    
    start_time = time.time()
    for i in range(total_actions):
        # 执行某个动作
        # ...

        elapsed_time = time.time() - start_time
        expected_time = total_time * (i+1) / total_actions
        remaining_time = expected_time - elapsed_time
        if remaining_time > 0:
            time.sleep(remaining_time)