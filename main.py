import ctypes
from ctypes import WinDLL
from ctypes.util import find_library

import usb.core
import usb.libloader

import platform

from platform_specific import setup_workarounds

setup_workarounds()

dev = usb.core.find(idVendor=0x18D1, idProduct=0x4EE1)  # Test device: Google Pixel 3A
print(dev)
