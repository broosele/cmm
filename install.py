""" Chipmunk manager

This module provides code to install chipmunk tools.

author: Bram Rooseleer
copyright: Bram Rooseleer
license: see license.txt
"""

import os

def add_parser(subparsers):
    parser = subparsers.add_parser('install', help="installs a tool")
    parser.add_argument('tool_name', help="the name of the tool to be installed")
    parser.add_argument('version', help="the version of the tool to be installed")
    parser.add_argument('--path', '-p', help="the path where the tool should be installed [default: pwd]", nargs='?', default=os.getcwd())
    try:
        repo = os.environ['cmm_repository']
    except KeyError:
        repo = 'No repo'
    parser.add_argument('-repository', '-r', help="metadata about the repository where the tools can be found [default: git "+repo+"]", nargs='+', default=['git', repo])
    parser.set_defaults(func=install)
    
def install(**args):
    print("Installing {tool_name} version {version} at {path}.".format(**args))