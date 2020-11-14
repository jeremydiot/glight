import sys

import usb

from commons.gLog import GLog


class GUsb:

    def __init__(self, vendorId, productId):

        self.device = usb.core.find(idVendor=vendorId, idProduct=productId)
        self.kernelDriverDetached = False

        if self.device is None:
            GLog().print_error("USB device not found")
            sys.exit(1)
        else:
            GLog().print_info("USB device found")

    def __attachDevice(self, wIndex):

        if self.device.is_kernel_driver_active(wIndex):
            self.device.detach_kernel_driver(wIndex)
            usb.util.claim_interface(self.device, wIndex)

        self.kernelDriverDetached = True
        GLog().print_info("device attached")

    def __detachDevice(self, wIndex):

        if self.kernelDriverDetached:
            usb.util.release_interface(self.device, wIndex)
            self.device.attach_kernel_driver(wIndex)

        self.kernelDriverDetached = False
        GLog().print_info("device dettached")

    def sendData(self, bmRequestType, bRequest, wValue, wIndex, data):

        self.__attachDevice(wIndex)

        self.device.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, data)
        GLog().print_info("data sended to device")

        self.__detachDevice(wIndex)
