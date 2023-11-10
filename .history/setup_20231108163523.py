##################################################

import os
import argparse
import yaml
from stream.flowinfo import FlowInfo, FlowCollection

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

    for flow in config['flows']:
        print(flow)
        flow = FlowInfo(flow['id'], flow['type'], flow['size'])
        print(flow)
    fc = FlowCollection()
