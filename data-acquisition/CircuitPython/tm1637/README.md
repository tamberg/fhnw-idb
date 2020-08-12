# Controlling a TM1637 4-digit display
How to control q TM1637 4-digit display with CircuitPython.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the "library" file [tm1637lib.py](tm1637lib.py) to the _CIRCUITPY_ drive.
* Copy the content of [tm1637.py](tm1637.py) to _code.py_ on the _CIRCUITPY_ drive.

## Hardware
* [Feather nRF52840 Express](https://github.com/tamberg/fhnw-idb/wiki/Feather-nRF52840-Express) microcontroller.
* [Grove shield for Feather](https://github.com/tamberg/fhnw-idb/wiki/Grove-Adapters#grove-shield-for-feather) to connect sensors.
* [4-digit display](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#4-digit-display-tm1637) wired to Grove _D4_ (nRF52840 _D9_ and _D10_).
