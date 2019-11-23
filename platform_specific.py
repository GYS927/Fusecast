import platform
from _ctypes import byref


def workaround_libusb_win():
    """
    Ideally, the use of this software on Windows should not require a permanent driver installation. LibUSB 1.0 supports
    a UsbDK backend, which should allow this. To load the LibUSB 1.0 driver, it must be present in ./lib/ relative to
    the current working directory. This workaround is successful, but there is some issue with LibUSB or UsbDK which
    makes PyUSB claim that the device is not found when performing a control transfer.
    :return:
    """
    import ctypes
    import pathlib
    import usb.backend.libusb1
    from ctypes import c_void_p, c_int

    # TOOD: Use logging module
    print('Fusecast: Using workaround to load libusb 1.0 DLL without installing it on Windows')

    dll_path = pathlib.Path.cwd() / 'lib' / 'libusb-1.0.dll'
    try:
        stdcall = ctypes.WinDLL(str(dll_path))
    except OSError:
        raise FileNotFoundError(
            f'Fusecast: Can\'t find libusb 1.0 DLL at {dll_path}. Check your current working directory.')

    if stdcall.__getattr__('libusb_init') is None:
        raise FileNotFoundError(f'Fusecast: Found libusb 1.0 DLL at {dll_path} but unable to verify. Does the '
                                f'architecture of the DLL match your Python installation?')
    else:
        print(f'Fusecast: Found libusb 1.0 DLL at {dll_path}')

    # Following code ripped out of PyUSB libusb 1.0 get_backend since it for some reason could not load the library (it
    # seemed to try to load as CDLL instead of WinDLL)
    usb.backend.libusb1._lib = stdcall # Replaces: _load_library(find_library=find_library)
    usb.backend.libusb1._setup_prototypes(usb.backend.libusb1._lib)
    backend = usb.backend.libusb1._LibUSB(usb.backend.libusb1._lib)

    # Enable UsbDK mode
    backend.lib.libusb_set_option.argtypes = [c_void_p, c_int]
    backend.lib.libusb_set_option(backend.ctx, 1)

    # TODO: The above code works, but sending a control transfer to the device results in the following stack trace:
    # https://gist.github.com/WardBenjamin/fee9a94561b7be5beff8e08497be3aec
    # NOTE: LibUSB 1.0.22 MS64, UsbDK 1.0-21, Python 3.8.0 x64, Windows 10 Pro x64
    # NOTE: See the following links:
    # https://github.com/daynix/UsbDk/issues/34
    # https://github.com/daynix/UsbDk/issues/5
    # https://github.com/pyusb/pyusb/issues/200

    # For this reason, development on Windows is currently halted


def setup_workarounds():
    if platform.system() is 'Windows':
        workaround_libusb_win()
