#!/usr/bin/env python3
import os
import argparse
import yaml
import logging

from stream.flowinfo import FlowInfo, FlowCollection
from stream.scheduler import FlowScheduler

parser = argparse.ArgumentParser(description='A flow generator for testing')
parser.add_argument('-c', '--config', type=str, required=True, help='config file path')

logging.basicConfig(filename='flows.log', 
                    filemode='w',
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

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

    flow_collections = []
    for flow in config['flows']:
        fc = FlowCollection(config[flow]['type'], 
                                config[flow]['num'], 
                                config[flow]['min_size'], 
                                config[flow]['max_size'], 
                                config[flow]['distribution'], 
                                config[flow]['distribution_params'])
        flow_collections.append(fc)
    
    scheduler = FlowScheduler(config['duration'], flow_collections[0].get_flows(), config['scheduler_p'])
    
    scheduler.run()
    

