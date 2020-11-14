import binascii

from src.commons.gUsb import GUsb
import src.constants as constants


class GDevice:
    def __init__(self, productId, bmRequestType, bRequest, wValue, wIndex):
        self.gUsb = GUsb(constants.ID_VENDOR, productId)
        self.constrolTransfertConfiguration = [bmRequestType, bRequest, wValue, wIndex]

        self.dataLenght = 40

    def sendDataToDevice(self, data):
        if len(data) != self.dataLenght:
            raise ValueError("data sended must be contain 40 characters, actually: "+str(len(data)))

        self.gUsb.sendData(*self.constrolTransfertConfiguration, binascii.unhexlify(data))

    def sendDataListToDevice(self, datas):
        for data in datas:
            self.sendDataToDevice(data)

    @staticmethod
    def brightnessToHex(brightnessArg):
        if(brightnessArg > 100 or brightnessArg < 1):
            brightnessArg = constants.DEFAULT_BRIGHTNESS

        return GDevice.decToHex(brightnessArg, 2)

    @staticmethod
    def frequencyToHex(frequencyArg):
        if(frequencyArg > 20000 or frequencyArg < 1000):
            frequencyArg = constants.DEFAULT_FREQUENCY

        return GDevice.decToHex(frequencyArg, 4)

    @staticmethod
    def colorToHex(colorArg):
        if colorArg:
            return GDevice.decToHex(int(colorArg, 16), 6)

        return constants.DEFAULT_COLOR

    @staticmethod
    def decToHex(decimal, length=6):
        if length == 6:
            return '%06x' % int(decimal)

        if length == 4:
            return '%04x' % int(decimal)

        if length == 2:
            return '%02x' % int(decimal)

        raise ValueError("wrong value for length: "+str(length))
