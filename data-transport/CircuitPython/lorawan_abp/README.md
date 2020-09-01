# Sending data to TheThingsNetwork with LoRaWAN
How to send data to TheThingsNetwork (TTN) with the Featherwing RFM95W LoRaWAN module.

## Running the example
### Get TTN keys
* Get a [TTN account](https://www.thethingsnetwork.org/), open the [TTN console](https://console.thethingsnetwork.org/) and add a [TTN application](https://console.thethingsnetwork.org/applications).
* Add a TTN *device*, change its *settings* to *Activation Method: ABP* and uncheck *Frame Counter Checks*.
* Check the the *settings* tab to get your TTN *Device Address*, *Network Session Key* and *App Session Key* (copy as *MSB*).

### Set up your device
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the [libraries](#Libraries) to the _lib_ directory on the _CIRCUITPY_ drive.
* Set *ttn_dev_address_msb*, *ttn_net_session_key_msb* and *ttn_app_session_key_msb* in the *lorawan_abp.py* example.
* Copy the content of [lorawan_abp.py](lorawan_abp.py) to _code.py_ on the _CIRCUITPY_ drive.

### See received data in TTN
* Check the *data* tab of your *device* in the [TTN console](https://console.thethingsnetwork.org/) to see incoming data packets.
* If no data shows up after 15 minutes, make sure you have [TTN network coverage](https://www.thethingsnetwork.org/community/).

### Decode received data in TTN
    function Decoder(bytes, port) { 
      var value = (bytes[0] << 8) | bytes[1];
      var json = {
        field1: value,
      }
      return json
    }

## Libraries
From the [CircuitPython libraries](https://circuitpython.org/libraries) bundle:
* Copy _lib/adafruit_tinylora/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa/) and [docs](https://circuitpython.readthedocs.io/projects/tinylora/en/latest/index.html)).
* Copy _lib/adafruit_bus_device/*_ (see [source](https://github.com/adafruit/Adafruit_CircuitPython_BusDevice/) and [docs](https://circuitpython.readthedocs.io/projects/busdevice/en/latest/index.html)).

## Hardware
### Required
* [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [FeatherWing RFM95W](https://github.com/tamberg/fhnw-idb/wiki/FeatherWing-RFM95W) LoRaWAN module.

### Optional
* [Grove shield for Feather](https://github.com/tamberg/fhnw-idb/wiki/Grove-Adapters#grove-shield-for-feather) to connect sensors.
* [Rotary angle sensor](https://github.com/tamberg/fhnw-idb/wiki/Grove-Sensors#rotary-angle-sensor) wired to Grove _A0_, or
* [Light sensor](https://github.com/tamberg/fhnw-idb/wiki/Grove-Sensors#light-sensor-v12) wired to Grove _A0_.

## Credits
* Based on https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa/tree/master/examples licensed under MIT License
