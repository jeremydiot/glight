defaultColor = "00A9E0"
defaultFrequency = 8000
defaultBrightness = 100

idVendor = 0x046D


def brightness(brightnessArg):
    if(brightnessArg > 100 or brightnessArg < 1):
        brightnessArg = defaultBrightness

    return brightnessArg


def frequency(frequencyArg):
    if(frequencyArg > 20000 or frequencyArg < 1000):
        frequencyArg = defaultFrequency

    return frequencyArg


def color(colorArg):

    if colorArg:
        return '%06x' % int(colorArg, 16)

    return defaultColor
