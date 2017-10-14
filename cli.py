#! /usr/bin/env python3.6

import sys

from address_to_coords import address_to_coords
from server import serve

# NOTE I would normally use something like `click` to make this CLI, but will
# remain consistent with the rest of the guidelines in only using built-in
# packages

def cli():
    help_text = """
    commands:
        help:                 prints this help text
        get_coords [address]: gets the coordinates for given address
        serve:                starts a server to listen for requests
    """
    
    incorrect_command_text = "incorrect command"

    num_args = len(sys.argv)

    if num_args > 1:
        command = sys.argv[1]
        if command == "help":
            print(help_text)
            return 0
        elif command == "get_coords" and num_args > 2:
            address = " ".join(sys.argv[2:])
            print(address_to_coords(address))
            return 0
        elif command == "serve":
            serve()
            return 0

    print(incorrect_command_text)
    print(help_text)
    return 1