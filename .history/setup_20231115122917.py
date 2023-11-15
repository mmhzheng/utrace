#!/usr/bin/env python3
import os
import argparse
import yaml
import logging
import time

from stream.flowinfo import FlowCollection
from stream.scheduler import FlowScheduler
from stream.serverbatch import ServerBatch

parser = argparse.ArgumentParser(description='A flow generator for testing')
parser.add_argument('-f', '--flow', type=str, required=True, help='flow config file path')
parser.add_argument('-s', '--server', type=str, required=True, help='server / client')

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

    schedule_time = config['duration']
    schedule_parallel = config['scheduler_p']
    flow_config = config['flows'] # Use get with a default empty dict
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
    
    # 将下面的代码用try catch包围，如果接收ctrl+c信号，就调用teardown_servers
    scheduler = FlowScheduler(schedule_time, fc, schedule_parallel)

    try:
        if args.mode == 'server':
            scheduler.setup_servers()
            time.sleep(3600)
        elif args.mode == 'client':
            scheduler.run()
        else:
            print(f"Invalid mode: {args.mode}")
            exit(1)
    except KeyboardInterrupt:
        if args.mode == 'server':
            scheduler.teardown_servers()
            exit(0)
