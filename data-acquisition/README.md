# Data Acquisition

1. [Intro](#intro)
2. [Resources](#resources)
3. [Reading sensor values](#reading-sensor-values)
4. [Controlling actuators](#controlling-actuators)
5. [CircuitPython examples](#circuitpython-examples)
6. [Python examples](#python-examples)

## Intro
> Data acquisition is the process of sampling signals that measure real world physical conditions and converting the resulting samples into digital numeric values that can be manipulated by a computer. 

--- from Wikipedia

## Resources
- Slides on [Microcontrollers, Sensors & Actuators](http://www.tamberg.org/fhnw/2020/hs/IdbMcuSensorsActuators.pdf).
- Slides [From Prototype to Connected Product](http://www.tamberg.org/fhnw/2020/hs/IdbPrototypeToProduct.pdf).
- [Grove Hardware Docs](https://github.com/Seeed-Studio/grove.py/tree/master/doc#gui-graphical-user-interface) with code examples.

## Reading sensor values
The available hardware includes a number of sensors:
* The [button](https://github.com/tamberg/fhnw-idb/wiki/Grove-Sensors#button) as an example of a digital sensor.
* The [DHT11](https://github.com/tamberg/fhnw-idb/wiki/Grove-Sensors#temperature--humidity-sensor-dht11), a common temperature and humidity sensor.
* A [light sensor](https://github.com/tamberg/fhnw-idb/wiki/Grove-Sensors#light-sensor-v12) and a [rotary angle sensor](https://github.com/tamberg/fhnw-idb/wiki/Grove-Sensors#rotary-angle-sensor) which are both analog sensors.

We will use these sensors as an example for:

* how to connect to the physical world?
* how to print out sensor values?
* how accurate the sensor is?
* how to deal with wrong values?
* how to visualize the data in a excel sheet and/or jupyter notebook?

## Controlling actuators
The available hardware includes the following actuators:

* The [buzzer](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#buzzer) and the [LED](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#led) as examples of digital actuators.
* The [chainable RGB LED](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#chainable-rgb-led) with a custom two-wire protocol.
* The [TM1637 4-digit display](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#4-digit-display-tm1637) with a custom onne-wire protocol.

These actuators can help to make a connected device easier to use.

## CircuitPython examples
First, try these examples with CircuitPython on the nRF52840:
* [Reading analog sensor input](CircuitPython/analog_input), e.g. light or rotation.
* [Reading digital sensor input](CircuitPython/digital_input), e.g. from a button.
* [Reading a DHT temperature & humidity sensor](CircuitPython/dht).

Then, add an actuator to provide some interactive feedback:
* [Controlling digital actuators](CircuitPython/digital_output), e.g. a buzzer or LED.
* [Controlling a chainable RGB LED](CircuitPython/grove_rgbled), e.g. to indicate states.
* [Controlling a TM1637 4-digit display](CircuitPython/tm1637), e.g. to show the time.

## Python examples
Try these examples with Circuit on the Raspberry Pi.

* [Reading a DHT temperature & humidity sensor](Python/dht).
