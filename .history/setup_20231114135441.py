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
    for flow in config.get('flows', []):  # Use get with a default empty list
        flow_config = config.get(flow, {})  # Use get with a default empty dict
        fc = FlowCollection(
            config.get('network', {}),
            flow_config['client']),
            flow_config.get('server_ip'),
            flow_config.get('server_port'),
            flow_config.get('type'), 
            flow_config.get('num'), 
            flow_config.get('min_size'), 
            flow_config.get('max_size'), 
            flow_config.get('distribution'), 
            flow_config.get('distribution_params')
        )
        flow_collections.append(fc)
    
    flows = []
    for fc in flow_collections:
        flows += fc.get_flows()
        
    scheduler = FlowScheduler(
        config.get('duration'), 
        flows, 
        config.get('scheduler_p')
    )
    
    scheduler.run()
