# -*- encoding: utf-8 -*-

"""Python Soundcloud Music Downloader."""

import os

__version__ = 'v1.6.12'
CLIENT_ID = 'a3e059563d7fd3372b49b37f00a00bcf'
ALT_CLIENT_ID = '2t9loNQH90kzJcsFCODdigxfp325aq4z'
ALT2_CLIENT_ID = 'NONE'

default_config = """[scdl]
auth_token =
path = .
premium_auth_token =
"""

config_dir = '.config'

config_file = os.path.join(config_dir, 'scdl.cfg')

if not os.path.exists(config_file):
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)

    with open(config_file, 'w') as f:
        f.write(default_config)
