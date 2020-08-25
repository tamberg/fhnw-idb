# Sending data to TheThingsNetwork with LoRaWAN
How to send data to TheThingsNetwork (TTN) with the Featherwing RFM95W LoRaWAN module.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the [libraries](#Libraries) to the _lib_ directory on the _CIRCUITPY_ drive.
* Get a [TTN account](https://www.thethingsnetwork.org/), open the [console](https://console.thethingsnetwork.org/), create an app and add a device.
* Set your TTN Device Address, Network Session Key and App Session Key in the lorawan_abp.py example.
* Copy the content of [lorawan_abp.py](lorawan_abp.py) to _code.py_ on the _CIRCUITPY_ drive.

## Libraries
From the [CircuitPython libraries](https://circuitpython.org/libraries) bundle:
* Copy _lib/adafruit_tinylora/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa/) and [docs](https://circuitpython.readthedocs.io/projects/tinylora/en/latest/index.html)).
* Copy _lib/adafruit_bus_device/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/) and [docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/index.html)).

## Hardware
* [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [FeatherWing RFM95W](https://github.com/tamberg/fhnw-idb/wiki/FeatherWing-RFM95W) LoRaWAN module.

## Credits
* Based on https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa/tree/master/examples licensed under MIT License
