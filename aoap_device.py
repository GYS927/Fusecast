import usb


class AndroidOpenAccessoryDevice:
    def __init__(self, vendor_id, product_id):
        self.vendor_id = vendor_id
        self.product_id = product_id
        self.device: usb.core.Device
        self.in_endpoint: usb.core.Endpoint
        self.out_endpoint: usb.core.Endpoint
        self._configure_device()

    def _configure_device(self):
        # Get the requested device handle
        self.device = usb.core.find(idVendor=self.vendor_id, idProduct=self.product_id)
        if self.device is None:
            return None, None, None

        # Get the input and output endpoints
        configuration = self.device.get_active_configuration()
        interface = configuration[(0, 0)]  # Use the first available interface
        self.in_endpoint = usb.util.find_descriptor(interface, custom_match=lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_IN)
        self.out_endpoint = usb.util.find_descriptor(interface, custom_match=lambda e: \
            usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)

        # Validate version code.
        buf = self.device.ctrl_transfer(0xc0, 51, data_or_wLength=2)
        print(len(buf))
        print(buf[0] | buf[1] << 8)
        # # Send accessory information.
        # for i, data in enumerate(
        #         (manufacturer, model, description, version, uri, serial)):
        #     assert (device.ctrl_transfer(
        #         0x40, 52, wIndex=i, data_or_wLength=data) == len(data))
        # # Put device into accessory mode.
        # assert (device.ctrl_transfer(0x40, 53) == 0)

    def is_valid(self):
        return self.device is not None and self.in_endpoint is not None and self.out_endpoint is not None
