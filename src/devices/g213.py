from commons.gDevice import GDevice
import constants


class G213(GDevice):
    def __init__(self):
        super().__init__(0xC336, 0x21, 0x09, 0x0211, 0x0001)

        self.dataPatterns = {
            "disable": "11ff0c3d00000000000000000000000000000000",
            "static": "11ff0c3d0{}01{}0200000000000000000000",
            "cycle": "11ff0c3d00030000000000{}64000000000000",
            "wave": "11ff0c3d0004000000000000{}{}{}00000000",
            "breathe": "11ff0c3d0002{}{}006400000000000000",
            "startEffect": "11ff0c5d00010{}00000000000000000000000000"}

    def disable(self):
        super().sendDataToDevice(self.dataPatterns["disable"])

    def static(self, *colors):
        keyboardZone = "0"

        if(len(colors) == 0):
            super().sendDataToDevice(self.dataPatterns["static"].format(
                keyboardZone, constants.DEFAULT_COLOR))

        elif(len(colors) == 1):
            super().sendDataToDevice(self.dataPatterns["static"].format(
                keyboardZone, GDevice.colorToHex(colors[0])))

        else:
            for i in range(1, 6):  # 1 to 5

                keyboardZone = str(i)
                color = constants.DEFAULT_COLOR

                if i <= len(colors):
                    color = super().colorToHex(colors[i-1])

                super().sendDataToDevice(self.dataPatterns["static"].format(
                    keyboardZone, color))

    def cycle(self, frequency=constants.DEFAULT_FREQUENCY):
        hexFrequency = GDevice.frequencyToHex(frequency)

        super().sendDataToDevice(self.dataPatterns["cycle"].format(hexFrequency))

    def wave(self, direction=0, frequency=constants.DEFAULT_FREQUENCY):
        directions = ["0164", "0664", "0364", "0864"]  # letf to right, right to left, center to edge, edge to center

        if direction > len(directions)-1 or direction < 0:
            direction = 0

        hexFrequency = GDevice.frequencyToHex(frequency)

        super().sendDataToDevice(self.dataPatterns["wave"].format(
            hexFrequency[-2:], directions[direction], hexFrequency[:2]))

    def breathe(self, color=constants.DEFAULT_COLOR, frequency=constants.DEFAULT_FREQUENCY):

        hexColor = GDevice.colorToHex(color)
        hexFrequency = GDevice.frequencyToHex(frequency)

        super().sendDataToDevice(self.dataPatterns["breathe"].format(hexColor, hexFrequency))

    def startEffect(self, state=True):

        value = "1"  # ON

        if not state:
            value = "2"  # OFF

        super().sendDataToDevice(self.dataPatterns["startEffect"].format(value))
