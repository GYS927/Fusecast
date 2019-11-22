# Fusecast
Android Auto headunit emulator for desktop Windows/Linux and Raspberry Pi

## Introduction

Fusecast was inspired by the [OpenAuto](https://github.com/f1xpl/openauto/) project by [Michal Szwaj (f1xpl)](https://github.com/f1xpl/), which is now abandoned since Michal seems to focus all of his time on the paid OpenAuto Pro. Excellent work was done by the [OpenCarDev team](https://github.com/opencardev) on [Crankshaft](https://github.com/opencardev/crankshaft) and their patched forks of OpenAuto and AASDK, but no one has much time to maintain that software. 

By moving to a Python-based implementation, which shares no code with OpenAuto, Fusecast aims to make development less complex and more open to community contributions. We rely on established libraries, such as PyUSB and PyBluez, where possible to abstract away much of the low-level platform-specific code, in turn simplifying application code.

Fusecast is a Work in Progress and is not currently functional!

## Installation

TODO: Windows libusb download, Linux udev rules

## Documentation

Future documentation will be posted to [ReadTheDocs](https://fusecast.rtfd.io)

## Reporting bugs/Submitting patches

Pull requests and bug reports are welcome. Please submit both of these via Github. 

For other inquiries, contact me at benjaminloganward@gmail.com. Cheers!

## Remarks

This software is created for R&D purposes only, and is not certified by Google. It may not work as expected, and features may change at any time. This is a work in progress. Do not use while driving. You use this software at your own risk.