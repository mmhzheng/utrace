#!/usr/bin/env python3
import os
import argparse
import yaml
import logging

from stream.flowinfo import FlowCollection
from stream.scheduler import FlowScheduler
from stream.serverbatch import ServerBatch

parser = argparse.ArgumentParser(description='A flow generator for testing')
parser.add_argument('-c', '--config', type=str, required=True, help='config file path')
parser.add_argument('-m', '--mode', type=str, required=True, help='server / client')

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

    flow_config = config[flows] # Use get with a default empty dict
    fc = FlowCollection(
        config['network'],
        flow_config['client'],
        flow_config['server_ip'],
        flow_config['server_port'],
        flow_config['type'], 
        flow_config['num'], 
        flow_config.get('distribution', None), 
        flow_config.get('distribution_params', None)
    )
    
    flows = fc.get_flows()
        
    if args.mode == 'server':
        serverbatch = ServerBatch(config['flows']['server_port'], config.get('server_p'))
    elif args.mode == 'client':
        scheduler = FlowScheduler(
            config.get('duration'), 
            flows, 
            config.get('scheduler_p')
        )
        scheduler.run()
    else:
        print(f"Invalid mode: {args.mode}")
        exit(1)

