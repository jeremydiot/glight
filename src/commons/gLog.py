"""
level 0 : no messages
level 1 : error
level 2 : error, debug
level 3 : error, debug, info

"""


class GLog():

    DEFAULT_LEVEL = 1

    def __init__(self, level=None):

        if isinstance(level, int) and level > -1 and level < 4:
            GLog.DEFAULT_LEVEL = level
            self.print_info("Log level "+str(level))

    def print_error(self, message):
        if GLog.DEFAULT_LEVEL > 0:
            print("/!\\ Error : " + message)

    def print_debug(self, message):
        if GLog.DEFAULT_LEVEL > 1:
            print("[x] Debug : " + message)

    def print_info(self, message):
        # self.frameinfo = getframeinfo(currentframe())
        if GLog.DEFAULT_LEVEL > 2:
            print("(i) Info: " + message)
