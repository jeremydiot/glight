import argparse

import src.constants as constants
from src.devices.g213 import G213 as G213Device


def define(subParsers):

    parserG213 = subParsers.add_parser("g213", help="g213 keyboard",
                                       formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parserG213.add_argument("--colors", nargs="+", type=str, default=[constants.DEFAULT_COLOR],
                            help="RRGGBB colors (000000 to FFFFFF) - 5 colors supported", metavar="RRGGBB")

    parserG213.add_argument("--frequency", type=int, default=constants.DEFAULT_FREQUENCY,
                            help="frequency milisecond (1000 to 200000)")

    parserG213.set_defaults(func=controller)

    groupG213 = parserG213.add_mutually_exclusive_group(required=True)

    groupG213.add_argument("--disable", help="turn off device lights",
                           action="store_true", default=argparse.SUPPRESS)

    groupG213.add_argument("--static", help="static lights mode - use: colors ",
                           action="store_true", default=argparse.SUPPRESS)

    groupG213.add_argument("--cycle", help="cycle lights mode - use: frequency",
                           action="store_true", default=argparse.SUPPRESS)

    groupG213.add_argument("--wave", help="wave lights mode - use: frequency",
                           default=argparse.SUPPRESS, nargs="?",
                           const=0, type=int, choices=range(0, 4))

    groupG213.add_argument("--breathe", help="breathe lights mode - use: colors and frequency",
                           action="store_true", default=argparse.SUPPRESS)

    groupG213.add_argument("--start-effect", help="switch on device start effect",
                           default=argparse.SUPPRESS, action="store_true")

    groupG213.add_argument("--no-start-effect", help="switch off device start effect",
                           default=argparse.SUPPRESS, action="store_false")


def controller(args):
    argsDict = vars(args)
    colors = argsDict["colors"]
    frequency = argsDict["frequency"]

    for key, value in argsDict.items():

        if(key == "disable"):
            G213Device().disable()

        elif(key == "static"):
            G213Device().static(*colors)

        elif(key == "cycle"):
            G213Device().cycle(frequency)

        elif(key == "wave"):
            G213Device().wave(value, frequency)

        elif(key == "breathe"):
            G213Device().breathe(colors[0], frequency)

        elif(key in ("start_effect", "no_start_effect")):
            G213Device().startEffect(value)

    return
