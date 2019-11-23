import usb.core
import time

from aoap_device import AndroidOpenAccessoryDevice
from platform_specific import setup_workarounds

setup_workarounds()

shutdown = False

# TODO: Add application structure
while not shutdown:
    # TODO: Search for all phones. Vendor list w/ IDs can be found in Crankshaft udev rules.
    # TODO: How to detect if a device is a phone?
    aoap_device = AndroidOpenAccessoryDevice(0x18D1, 0x4EE1)  # Test device: Google Pixel 3A
    if aoap_device.is_valid():
        shutdown = True
    time.sleep(0.1)

print(aoap_device.device)
