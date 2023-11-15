#!/usr/bin/env python3
import os
import argparse
import yaml
import logging
import time

from stream.flowinfo import FlowCollection
from stream.scheduler import FlowScheduler

logging.basicConfig(filename='flows.log', 
                    filemode='w',
                    level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='A flow generator for testing')
parser.add_argument('-f', '--flow_cfg', type=str, required=True, help='flow config file path')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', '--server', action='store_true', help='Run as server')
group.add_argument('-c', '--client', action='store_true', help='Run as client')


if __name__ == '__main__':
    
    args = parser.parse_args()
    
    # read yaml file
    config_file = args.flow_cfg
    if not os.path.exists(config_file):
        print(f"No such file: {config_file}")
        exit(1)
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)

    # setup flow collection
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
    
    schedule_time = config['duration']
    schedule_parallel = config['scheduler_p']
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
