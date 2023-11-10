#!/usr/bin/env python3
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
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    fc = {}
    for flow in config['flows']:
        fc = FlowCollection(config[flow]['type'], 
                            config[flow]['num'], 
                            config[flow]['min_size'], 
                            config[flow]['max_size'], 
                            config[flow]['distribution'], 
                            config[flow]['distribution_params'])
        

