# Data Acquisition

1. [Intro](#intro)
2. [Resources](#resources)
3. [Temperature & Humidity](#temperature-&-humidity)
4. [CircuitPython examples](#circuitpython-examples)
5. [Python examples](#python-examples)

## Intro

> Data acquisition is the process of sampling signals that measure real world physical conditions and converting the resulting samples into digital numeric values that can be manipulated by a computer. 

--- from Wikipedia

## Resources

- Slides on [Microcontrollers, Sensors & Actuators](http://www.tamberg.org/fhnw/2020/hs/IdbMcuSensorsActuators.pdf).
- Slides [From Prototype to Connected Product](http://www.tamberg.org/fhnw/2020/hs/IdbPrototypeToProduct.pdf).
- [Grove Hardware Docs](https://github.com/Seeed-Studio/grove.py/tree/master/doc#gui-graphical-user-interface) with code examples.

## Reading sensor values

[DHT11](https://github.com/tamberg/fhnw-iot/wiki/Grove-Sensors#temperature--humidity-sensor-dht11) is a common temperature and humidity sensor.

We will use these sensors as an example for

- how to connect to the physical world?
- how to print out sensor values?
- how accurate the sensor is?
- how to deal with wrong values?
- how to visualize the data in a excel sheet and/or jupyter notebook?

## CircuitPython examples
Try these examples with CircuitPython on the nRF52840.

* [Reading a DHT temperature & humidity sensor](CircuitPython/dht)

## Python examples
Try these examples with Circuit on the Raspberry Pi.

* [Reading a DHT temperature & humidity sensor](Python/dht)
