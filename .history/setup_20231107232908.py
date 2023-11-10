import yaml





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
