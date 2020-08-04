# Scan Wi-Fi networks
How to scan Wi-Fi networks with the FeatherWing ESP32 AirLift Wi-Fi module.

## Libraries
Part of [https://circuitpython.org/libraries](https://circuitpython.org/libraries) unless noted otherwise.
* https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/ ([Docs](https://circuitpython.readthedocs.io/projects/esp32spi/en/latest/index.html))
* https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/ ([Docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/index.html))

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
