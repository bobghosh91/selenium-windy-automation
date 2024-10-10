import configparser
import os
import pdb


def read_config():
    config = configparser.RawConfigParser()
    config_file_path = os.path.join(os.getcwd(), 'configs', 'config.ini')
    config.read(config_file_path)
    return config['DEFAULT']


# Example usage Read config.ini file
# config_data = read_config()
# print(config_data['url'])
