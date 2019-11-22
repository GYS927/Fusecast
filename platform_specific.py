import platform


def workaround_libusb_win():
    import ctypes
    import pathlib
    import usb.backend.libusb1

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
    usb.backend.libusb1._lib = stdcall


def setup_workarounds():
    if platform.system() is 'Windows':
        workaround_libusb_win()
