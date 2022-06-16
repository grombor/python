import configparser
from datetime import datetime

# Server config variables
config = configparser.ConfigParser()
config.sections()
config.read('.\\server_files\\server_config.ini')

# Assign data to variables
_HOST = str(config['DEFAULT']['HOST'])
_PORT = int(config['DEFAULT']['PORT'])
_HEADER_SIZE = int(config['DEFAULT']['HEADER_SIZE'])
_CODING = str(config['DEFAULT']['CODING'])
_VERSION = str(config['DEFAULT']['VERSION'])


def get_config():
    """ Get HOST, PORT, HEADER_SIZE and CODING"""
    return _HOST, _PORT, _HEADER_SIZE, _CODING


def get_version():
    """ Get server version """
    return _VERSION

def get_uptime():
    """ Get server uptime """
    uptime = datetime.now()
    return uptime
