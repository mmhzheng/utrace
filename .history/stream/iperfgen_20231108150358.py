from stream.flowgen import FlowGenerator
from stream.flowinfo import FlowInfo
import subprocess

# def run_command(command):
#     

# # 示例命令：获取当前目录下的文件列表
# command = 'ls'

# # 运行命令并获取输出
# output = run_command(command)


class IperfClient(FlowGenerator):
    def __init__(self):
        self.tasks = []

    def lauch_one_flow(flow : FlowInfo) -> None:
        id = flow.id
        size = flow.size
        command = f''
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, _ = process.communicate()
        return output.decode('utf-8')
 