import sys
import argparse

import glight.constants as constants
import glight.cli.g213 as g213Cli
import glight.cli.g403hero as g403heroCli


def main():

    parser = argparse.ArgumentParser(prog=constants.PROGRAM_NAME, description='Control Logitech devices light.')

    subParsers = parser.add_subparsers(help="logitech devices")

    # register cli command for each device
    g213Cli.define(subParsers)
    g403heroCli.define(subParsers)

    if(len(sys.argv[1:]) == 0):
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args(sys.argv[1:])
    args.func(args)


if __name__ == '__main__':
    main()
