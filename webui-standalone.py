#!/usr/bin/env python
import os
import argparse
import webui

DEFAULT_CONFIG = {
    'host': "127.0.0.1",
    'port': 8080
}

config = {
    'host': "0.0.0.0",
    'port': 8088
}

# handle command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--addr', default=DEFAULT_CONFIG['host'],help='address to bind to [127.0.0.1]')
parser.add_argument('-p', '--port', default=DEFAULT_CONFIG['port'],type=int, help='port to listen on [8080]')
args = parser.parse_args()

# change to webui's directory and import
if os.path.dirname(__file__) != "":
    os.chdir(os.path.dirname(__file__))

if args.addr != '127.0.0.1':
    config['host'] = args.addr
else:
    config['host'] = "0.0.0.0"
print(args.port)

if args.port != 8080:
    config['port'] = args.port
else:
    config['port'] = 8088

# set up webui and run in own http server
webui.bottle.debug(True)
webui.bottle.run(host=config['host'], port=config['port'], reloader=False)

# vim: foldmethod=marker:filetype=python:textwidth=80:ts=4:et
