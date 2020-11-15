import argparse
import src.constants as constants

from src.devices.g403hero import G403Hero as G403HeroDevice


def define(subParsers):

    parserG403hero = subParsers.add_parser("g403hero", help="g403-hero mouse",
                                           formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parserG403hero.add_argument("--zone", help="mouse zone", type=str, choices=["all", "logo", "scroll"],
                                default="all")

    parserG403hero.add_argument("--color", help="RRGGBB colors (000000 to FFFFFF)",
                                type=str, default=constants.DEFAULT_COLOR, metavar="RRGGBB")

    parserG403hero.add_argument("--frequency", help="frequency milisecond (1000 to 200000)",
                                type=int, default=constants.DEFAULT_FREQUENCY)

    parserG403hero.add_argument("--brightness", help="brightness percent (1 to 100)",
                                type=int, default=constants.DEFAULT_BRIGHTNESS)

    parserG403hero.set_defaults(func=controller)

    groupG403hero = parserG403hero.add_mutually_exclusive_group(required=True)

    groupG403hero.add_argument("--disable", help="turn off device lights",
                               action='store_true', default=argparse.SUPPRESS)

    groupG403hero.add_argument("--static", help="static lights mode - use: color ",
                               action='store_true', default=argparse.SUPPRESS)

    groupG403hero.add_argument("--cycle", help="cycle lights mode - use: frequency and brightness",
                               action='store_true', default=argparse.SUPPRESS)

    groupG403hero.add_argument("--breathe", help="breathe lights mode - use: color, frequency, and brightness",
                               action='store_true', default=argparse.SUPPRESS)

    groupG403hero.add_argument("--start-effect", help="switch on device start effect",
                               default=argparse.SUPPRESS, action='store_true')

    groupG403hero.add_argument("--no-start-effect", help="switch off device start effect",
                               default=argparse.SUPPRESS, action='store_false')


def controller(args):
    argsDict = vars(args)
    zone = argsDict["zone"]

    if (zone == "all"):
        zone = None
    elif (zone == "scroll"):
        zone = 0
    elif (zone == "logo"):
        zone = 1

    color = argsDict["color"]
    frequency = argsDict["frequency"]
    brightness = argsDict["brightness"]

    for key, value in argsDict.items():

        if(key == "disable"):
            G403HeroDevice(zone).disable()

        elif(key == "static"):
            G403HeroDevice(zone).static(color)

        elif(key == "cycle"):
            G403HeroDevice(zone).cycle(frequency, brightness)

        elif(key == "breathe"):
            G403HeroDevice(zone).breathe(color, frequency, brightness)

        elif(key in ("start_effect", "no_start_effect")):
            G403HeroDevice(zone).startEffect(value)

    return
