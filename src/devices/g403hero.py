import binascii

from commons.gUsb import GUsb
import utils.dataController as dataController
import utils.dataFormatter as dataFormatter

idProduct = 0xC08f  # id product of G403hero mouse

# control transfert configuration
bmRequestType = 0x21
bRequest = 0x09
wValue = 0x0211
wIndex = 0x0001

gUsb = GUsb(dataController.idVendor, idProduct)


def disable(element=None):
    dataPattern = ["11ff0e3d01000000000000000000000000000000",  # logo
                   "11ff0e3d00000000000000000000000000000000"]  # scroll wheel

    dataPattern = __elementControl(dataPattern, element)

    for data in dataPattern:
        gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(data))


def static(color=dataController.defaultColor, element=None):
    dataPattern = ["11ff0e3d0101{}0200000000000000000000",  # logo
                   "11ff0e3d0001{}0200000000000000000000"]  # scroll wheel

    dataPattern = __elementControl(dataPattern, element)

    for data in dataPattern:
        gUsb.sendData(bmRequestType, bRequest, wValue, wIndex,
                      binascii.unhexlify(data.format(dataController.color(color))))


def cycle(frequency=dataController.defaultFrequency,
          brightness=dataController.defaultBrightness, element=None):
    dataPattern = ["11ff0e3d01020000000000{}000000000000",  # logo
                   "11ff0e3d00020000000000{}000000000000"]  # scroll wheel

    dataPattern = __elementControl(dataPattern, element)

    frequency = dataController.frequency(frequency)
    hexFrequency = dataFormatter.decToHex(frequency, 4)

    brightness = dataController.brightness(brightness)
    hexBrightness = dataFormatter.decToHex(brightness, 2)

    for data in dataPattern:
        gUsb.sendData(bmRequestType, bRequest, wValue, wIndex,
                      binascii.unhexlify(data.format(hexFrequency+hexBrightness)))


def breathe(color=dataController.defaultColor, frequency=dataController.defaultFrequency,
            brightness=dataController.defaultBrightness, element=None):
    dataPattern = ["11ff0e3d0103{}00{}00000000000000",  # logo
                   "11ff0e3d0003{}00{}00000000000000"]  # scroll wheel

    dataPattern = __elementControl(dataPattern, element)

    frequency = dataController.frequency(frequency)
    hexFrequency = dataFormatter.decToHex(frequency, 4)

    brightness = dataController.brightness(brightness)
    hexBrightness = dataFormatter.decToHex(brightness, 2)

    for data in dataPattern:
        gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
            data.format(dataController.color(color)+hexFrequency, hexBrightness)))


def startEffect(state=True):
    dataPattern = "11ff0e5d00010{}00000000000000000000000000"
    data = ""

    if state:
        data = dataPattern.format("1")
    else:
        data = dataPattern.format("2")

    gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(data))


def __elementControl(dataPattern, element):
    if (element is not None and element < len(dataPattern) and element > -1):
        return [dataPattern[element]]

    return dataPattern
