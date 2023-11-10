from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess


class IperfClient(FlowGenerator):
    def __init__(self):
        self.tasks = []

    def lauch_one_flow(flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        command = f'ls -l'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        return output.decode('utf-8')
 