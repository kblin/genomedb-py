# vim: set fileencoding=utf-8 :
"""genomedb - configuration settings

default settings are collected here, as well as some utility functions
"""

import ConfigParser
from os import path
from argparse import Namespace

_defaults = {
    'db': 'sqlite:///genome.db',
}

_user_file_name = path.expanduser('~/.genomedb.cfg')

def load_config(options):
    """Load configuration from a config file in the user's home directory.
    Fall back to defaults for missing settings.
    """
    # create a parser providing default values
    config = ConfigParser.ConfigParser(_defaults)

    # read the user config file if present, ignoring errors
    config.read([_user_file_name])

    for s in config.sections():
        if s not in options:
            options.__dict__[s] = Namespace()
        for key, val in config.items(s):
            key = key.replace('-', '_')
            if key not in options.__dict__[s]:
                options.__dict__[s].__dict__[key] = val


    # [DEFAULT] entries go to the global namespace
    for key, val in config.items('DEFAULT'):
        key = key.replace('-', '_')
        if key not in options:
            options.__dict__[key] = val
