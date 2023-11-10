##################################################

import os
import argparse
import yaml

parser = argparse.ArgumentParser(description='A flow generator for testing')
parser.add_argument('-c', '--config', type=str, required=True, help='config file path')


if __name__ == '__main__':
    
    # Check if the config file exists
    args = parser.parse_args()
    config_file = args.config
    if not os.path.exists(config_file):
        print(f"No such file: {config_file}")
        exit(1)

    # read yaml file
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
