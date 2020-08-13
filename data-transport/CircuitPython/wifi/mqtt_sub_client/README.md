# Subscribing to a MQTT topic
How to subscribe to a MQTT topic with the FeatherWing ESP32 AirLift Wi-Fi module.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the [libraries](#Libraries) to the _lib_ directory on the _CIRCUITPY_ drive.
* Set your Wi-Fi _ssid_ and _password_ in the [mqtt_sub_client.py](mqtt_sub_client.py) example.
* Copy the content of [mqtt_sub_client.py](mqtt_sub_client.py) to _code.py_ on the _CIRCUITPY_ drive.

## Libraries
From the [CircuitPython libraries](https://circuitpython.org/libraries) bundle:
* Copy _lib/adafruit_bus_device/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/) and [docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/)).
* Copy _lib/adafruit_esp32spi/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_ESP32SPI/) and [docs](https://circuitpython.readthedocs.io/projects/esp32spi/en/latest/)).
* Copy _lib/adafruit_logging.mpy_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_Logging) and [docs](https://circuitpython.readthedocs.io/projects/logging/en/latest/)).
* Copy _lib/adafruit_minimqtt/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT/) and [docs](https://circuitpython.readthedocs.io/projects/minimqtt/en/latest/)).

## Hardware
* [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [FeatherWing ESP32 AirLift](https://github.com/tamberg/fhnw-idb/wiki/FeatherWing-ESP32-AirLift) Wi-Fi module.

## Credits
* Based on https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT/tree/master/examples licensed under MIT License
