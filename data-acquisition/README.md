# Data Acquisition

1. [Intro](#intro)
2. [Resources](#resources)
3. [Temperature & Humidity](#temperature-&-humidity)
4. [DHT with MicroPython on ESP8266](esp8266)
5. [DHT with Python on Raspberry Pi](raspberry)

## Intro

> Data acquisition is the process of sampling signals that measure real world physical conditions and converting the resulting samples into digital numeric values that can be manipulated by a computer. 

--- from Wikipedia

## Resources

- Slides on [Microcontrollers, Sensors & Actuators](http://www.tamberg.org/fhnw/2020/hs/IdbMcuSensorsAndActuators.pdf).
- Slides [From Prototype to Connected Product](http://www.tamberg.org/fhnw/2020/hs/IdbPrototypeToProduct.pdf).
- [Grove Hardware Docs](https://github.com/Seeed-Studio/grove.py/tree/master/doc#gui-graphical-user-interface) with code examples.

## Temperature & Humidity

[DHT11](https://github.com/tamberg/fhnw-iot/wiki/Grove-Sensors#temperature--humidity-sensor-dht11) is the most common temperature and humidity module for Arduino and Raspberry Pi.

We will use this sensor as an example for

- how to connect to the physical world?
- how to print out these sensor values?
- how accurate the sensor is?
- how to deal with wrong values?
- how to create and visualize an excel sheet/diagram?
