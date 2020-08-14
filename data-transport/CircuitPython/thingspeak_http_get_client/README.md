# Reading from the REST API on ThingSpeak
How to read data from ThingSpeak's REST API with the FeatherWing ESP32 AirLift Wi-Fi module.

Consult [Read Data](https://ch.mathworks.com/help/thingspeak/readdata.html) to get info about each Query String Parameter which is supported by the REST API.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the [libraries](#Libraries) to the _lib_ directory on the _CIRCUITPY_ drive.
* Set your Wi-Fi and your ThingSpeak settings in [thingspeak_http_get_client.py](thingspeak_http_get_client.py) settings.
* Copy the content of your _thingspeak_http_get_client.py_ to _code.py_ on the _CIRCUITPY_ drive.


## Libraries
From the [CircuitPython libraries](https://circuitpython.org/libraries) bundle:
* Copy _lib/adafruit_esp32spi/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/) and [docs](https://circuitpython.readthedocs.io/projects/esp32spi/en/latest/index.html)).
* Copy _lib/adafruit_bus_device/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/) and [docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/index.html)).
* Copy _lib/adafruit_requests_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_Requests/) and [docs](https://circuitpython.readthedocs.io/projects/requests/en/latest/index.html)).

## Hardware
* [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [FeatherWing ESP32 AirLift](https://github.com/tamberg/fhnw-idb/wiki/FeatherWing-ESP32-AirLift) Wi-Fi module.

## Credits
* Based on https://circuitpython.readthedocs.io/projects/requests/en/latest/examples.html licensed under MIT License
