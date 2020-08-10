# Introduction to the Internet of Things
1. [Overview](#overview)
1. [Intro](#intro)
2. [Resources](#resources)
3. [Python vs. MicroPython vs. CircuitPython](#python-vs-micropython-vs-circuitpython)
4. [Getting Started with CircuitPython on nRF52840](#getting-started-with-circuitpython-on-nrf52840)
5. [Getting Started with Python on Raspberry Pi](#getting-started-with-python-on-raspberry-pi)

## Overview

This introduction should enable you to set up and use your computer in a way that makes getting started with IoT easy.

We will be using different hardware, so you can finally answer the following questions:

* how IoT hardware is connected to your computer?
* how is possible to program for a IoT hardware?
* how does IoT hardware differ?

## Intro

> The IoT creates opportunities for more direct integration of the physical world into computer-based systems, resulting in efficiency improvements, economic benefits, and reduced human exertions.

— Quote from [Wikipedia](https://en.wikipedia.org/wiki/Internet_of_things#Trends_and_characteristics)

## Resources

- Slides [Introduction to the Internet of Things](http://www.tamberg.org/fhnw/2020/hs/IdbInternetOfThings.pdf).

## Python vs. MicroPython vs. CircuitPython

> Finally, Python had moved off of desktops and servers and into the world of sensors, actuators, motors, LCD displays, buttons, and circuits. While this presented many challenges, there were also copious opportunities. Desktop and server hardware requires gigahertz processors, gigabytes of RAM, and terabytes of storage. They also need fully-fledged operating systems, device drivers, and true multitasking.
>
> In the microcontroller world, however, MicroPython is the operating system.

— Quote from [MicroPython: An Intro to Programming Hardware in Python](https://realpython.com/micropython/)

> MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

— Quote from the [MicroPython Website](https://micropython.org/)

> CircuitPython is a programming language designed to simplify experimenting and learning to code on low-cost microcontroller boards. [It] wouldn't exist without the awesome work of Damien George and the MicroPython community.

— Quote from the [CircuitPython Website](https://circuitpython.org/)

**Note:** We will use CircuitPython for our labs and examples. The entry into microprocessor programming is easiest with CircuitPython.

### Developing with CircuitPython

Check the following points:

- Choose an editor: We recommend the **Mu-editor** which can be downloaded from https://codewith.mu/. Mu is easy to use and have included a serial console, which is needed to see `print()` statements.

    Note for Mac Users with Catalina OSX:  
    Start the application for the first time with CTRL Key pressed to be able to accept the security restrictions be the macos.

    You will find in [this chapter](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code#1-use-an-editor-that-writes-out-the-file-completely-when-you-save-it-2977444-16) other editors, which are suitable for CircuitPython programming.

- Connect the Feather nRF52840 Express via USB to your computer. Check if you see the `CIRCUITPY` drive on your desktop.

The **CircuitPython Reference Docs** can be found on https://circuitpython.readthedocs.io/en/latest/README.html

## Getting Started with CircuitPython on nRF52840
Follow the steps in [Getting Started with CircuitPython on nRF52840](CircuitPython)

## Getting Started with Python on Raspberry Pi
Follow the steps in [Getting Started with Python on Raspberry Pi](Python)
