from commons.gDevice import GDevice
import constants


class G403Hero(GDevice):
    def __init__(self, part=None):
        super().__init__(0xC08f, 0x21, 0x09, 0x0211, 0x0001)

        self.dataPatterns = {
            "disable": ["11ff0e3d01000000000000000000000000000000",     # logo
                        "11ff0e3d00000000000000000000000000000000"],    # scroll whell
            "static": ["11ff0e3d0101{}0200000000000000000000",
                       "11ff0e3d0001{}0200000000000000000000"],
            "cycle": ["11ff0e3d01020000000000{}{}000000000000",
                      "11ff0e3d00020000000000{}{}000000000000"],
            "breathe": ["11ff0e3d0103{}{}00{}00000000000000",
                        "11ff0e3d0003{}{}00{}00000000000000"],
            "startEffect": "11ff0c5d00010{}00000000000000000000000000"}

        if (part == 0 or part == 1):
            for key, value in self.dataPatterns.items():
                if isinstance(value, list):
                    del value[part]

    def disable(self):
        super().sendDataListToDevice(self.dataPatterns["disable"])

    def static(self, color=constants.DEFAULT_COLOR):
        for data in self.dataPatterns["static"]:
            super().sendDataToDevice(data.format(GDevice.colorToHex(color)))

    def cycle(self, frequency=constants.DEFAULT_FREQUENCY, brightness=constants.DEFAULT_BRIGHTNESS):

        hexFrequency = GDevice.frequencyToHex(frequency)
        hexBrightness = GDevice.brightnessToHex(brightness)

        for data in self.dataPatterns["cycle"]:
            super().sendDataToDevice(data.format(hexFrequency, hexBrightness))

    def breathe(self, color=constants.DEFAULT_COLOR, frequency=constants.DEFAULT_FREQUENCY,
                brightness=constants.DEFAULT_BRIGHTNESS):

        hexColor = GDevice.colorToHex(color)
        hexFrequency = GDevice.frequencyToHex(frequency)
        hexBrightness = GDevice.brightnessToHex(brightness)

        for data in self.dataPatterns["breathe"]:
            super().sendDataToDevice(data.format(hexColor, hexFrequency, hexBrightness))

    def startEffect(self, state=True):

        value = "1"  # ON

        if not state:
            value = "2"  # OFF

        super().sendDataToDevice(self.dataPatterns["startEffect"].format(value))
