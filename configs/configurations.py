import configparser
import os


CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'config.ini')


def read_config():
    config = configparser.RawConfigParser()
    config.read(CONFIG_PATH)

    # Credentials deliberately come from the environment rather than a file
    # that can be committed to source control or included in build artifacts.
    values = dict(config['DEFAULT'])
    values['url'] = os.getenv('WINDY_URL', values.get('url', 'https://www.windy.com/'))
    values['email'] = os.getenv('WINDY_EMAIL', '')
    values['password'] = os.getenv('WINDY_PASSWORD', '')
    return values


# Example usage Read config.ini file
# config_data = read_config()
# print(config_data['url'])
