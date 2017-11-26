""" Chipmunk manager

This script interprets cmm commands and executes them.

author: Bram Rooseleer
copyright: Bram Rooseleer
license: see license.txt
"""

import argparse
import install

parser = argparse.ArgumentParser(description="Manager for chipmunk tool installations.", prog='cmm', epilog="see license.txt")
parser.add_argument('--version', action='version', version="%(prog)s 0")
subparsers = parser.add_subparsers(title="Available subcommands", help="choose one of these")

install.add_parser(subparsers)

args = parser.parse_args()
try:
    args.func(**vars(args))
except AttributeError:
    parser.parse_args(["-h"])