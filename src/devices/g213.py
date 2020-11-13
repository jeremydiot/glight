import binascii

from commons.gUsb import GUsb
import utils.dataController as dataController
import utils.dataFormatter as dataFormatter

idProduct = 0xC336  # id product of G213 keyboard

# control transfert configuration
bmRequestType = 0x21
bRequest = 0x09
wValue = 0x0211
wIndex = 0x0001


gUsb = GUsb(dataController.idVendor, idProduct)  # usb python module


def disable():
    data = "11ff0c3d00000000000000000000000000000000"
    gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(data))


def static(*colors):
    keyboardZone = "0"
    dataPattern = "11ff0c3d0{}01{}0200000000000000000000"

    if len(colors) == 0:
        gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
            dataPattern.format(keyboardZone, dataController.defaultColor)))

    elif len(colors) == 1:
        gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
            dataPattern.format(keyboardZone, dataController.color(colors[0]))))

    else:
        for i in range(1, 6):

            keyboardZone = str(i)
            color = dataController.defaultColor

            if i <= len(colors):
                color = dataController.color(colors[i-1])

            gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
                dataPattern.format(keyboardZone, color)))


def cycle(frequency=dataController.defaultFrequency):
    dataPattern = "11ff0c3d00030000000000{}64000000000000"

    frequency = dataController.frequency(frequency)
    hexFrequency = dataFormatter.decToHex(frequency, 4)

    gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
        dataPattern.format(hexFrequency)))


def wave(direction=0, frequency=dataController.defaultFrequency):
    dataPattern = "11ff0c3d0004000000000000{}00000000"
    directions = ["0164", "0664", "0364", "0864"]  # letf to right, right to left, center to edge, edge to center

    frequency = dataController.frequency(frequency)
    hexFrequency = dataFormatter.decToHex(frequency, 4)

    if direction > len(directions)-1 or direction < 0:
        direction = 0

    gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
        dataPattern.format(hexFrequency[-2:]+directions[direction]+hexFrequency[:2])))


def breathe(color=dataController.defaultColor, frequency=dataController.defaultFrequency):
    dataPattern = "11ff0c3d0002{}006400000000000000"

    frequency = dataController.frequency(frequency)
    hexFrequency = dataFormatter.decToHex(frequency, 4)

    gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(
        dataPattern.format(dataController.color(color)+hexFrequency)))


def startEffect(state=True):
    dataPattern = "11ff0c5d00010{}00000000000000000000000000"
    data = ""

    if state:
        data = dataPattern.format("1")
    else:
        data = dataPattern.format("2")

    gUsb.sendData(bmRequestType, bRequest, wValue, wIndex, binascii.unhexlify(data))
