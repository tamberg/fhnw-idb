# Data Acquisition

1. [Intro](#intro)
2. [Resources](#resources)
3. [Temperature & Humidity](#temperature-&-humidity)
4. [DHT with MicroPython on ESP8266](#dht-with-micropython-on-esp8266)
5. [DHT with Python on Raspberry Pi](#dht-with-micropython-on-raspberry-pi)

## Intro

> Data acquisition is the process of sampling signals that measure real world physical conditions and converting the resulting samples into digital numeric values that can be manipulated by a computer. 

--- from Wikipedia

## Resources

- Slides on [Microcontrollers, Sensors & Actuators](http://www.tamberg.org/fhnw/2020/hs/IdbMcuSensorsActuators.pdf).
- Slides [From Prototype to Connected Product](http://www.tamberg.org/fhnw/2020/hs/IdbPrototypeToProduct.pdf).
- [Grove Hardware Docs](https://github.com/Seeed-Studio/grove.py/tree/master/doc#gui-graphical-user-interface) with code examples.

## Temperature & Humidity

[DHT11](https://github.com/tamberg/fhnw-iot/wiki/Grove-Sensors#temperature--humidity-sensor-dht11) is the most common temperature and humidity module for Arduino and Raspberry Pi.

We will use this sensor as an example for

- how to connect to the physical world?
- how to print out these sensor values?
- how accurate the sensor is?
- how to deal with wrong values?
- how to visualize the data in a excel sheet and/or jupyter notebook?

## DHT with MicroPython on ESP8266
Follow the steps in [DHT with MicroPython on ESP8266](esp8266)

## DHT with Python on Raspberry Pi
Follow the steps in [DHT with Python on Raspberry Pi](raspberry)
