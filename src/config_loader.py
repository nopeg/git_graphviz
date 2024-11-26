import configparser

def load_config(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)

    config = {
        'graphviz_path': config.get('configuration', 'graphviz_path'),
        'repo_path': config.get('configuration', 'repo_path'),
        'output_path': config.get('configuration', 'output_path'),
        'branch_name': config.get('configuration', 'branch_name')
    }
    return config
