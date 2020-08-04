# Scanning Wi-Fi networks
How to scan Wi-Fi networks with the FeatherWing ESP32 AirLift Wi-Fi module.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the [libraries](#Libraries) to the _lib_ directory on the _CIRCUITPY_ drive.
* Copy the content of [wifi_scan.py](wifi_scan.py) to _code.py_ on the _CIRCUITPY_ drive.

## Libraries
Part of the [https://circuitpython.org/libraries](https://circuitpython.org/libraries) bundle:
* https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/ (see [docs](https://circuitpython.readthedocs.io/projects/esp32spi/en/latest/index.html)).
* https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/ (see [docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/index.html)).

## Hardware
* [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [FeatherWing ESP32 AirLift](https://github.com/tamberg/fhnw-idb/wiki/FeatherWing-ESP32-AirLift) Wi-Fi module.

### Mapping
ESP32|nRF52840 (or M4)
:---|:---
CS |D13
RDY |D11
RST |D12

## Credits
* Based on https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/ licensed under MIT License
