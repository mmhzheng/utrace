import os
import argparse
import yaml

# 创建参数解析器
parser = argparse.ArgumentParser(description='解析参数示例')
parser.add_argument('-c', '--config', type=str, required=True, help='配置文件路径')

# 解析参数
args = parser.parse_args()

# 检查文件路径是否存在
config_file = args.config
if not os.path.exists(config_file):
    print(f"文件路径不存在：{config_file}")
    exit(1)

# 执行其他操作，比如读取配置文件内容
with open(config_file, 'r') as file:
    config_data = file.read()
    # 在这里处理配置文件数据

# 输出结果
print(f"配置文件路径：{config_file}")




if __name__ == '__main__':
    # 读取 YAML 文件
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # 访问配置项
    database_host = config['database']['host']
    database_port = config['database']['port']
    server_host = config['server']['host']
    server_port = config['server']['port']

    # 打印配置项
    print(f"Database host: {database_host}")
    print(f"Database port: {database_port}")
    print(f"Server host: {server_host}")
    print(f"Server port: {server_port}")
