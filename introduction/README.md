# IoT Introduction
1. [Documentation](#documentation)
2. [MicroPython](#micropython)
3. [Developing with MicroPython](#developing-with-microPython)
4. [Installation on Microcontroller Boards](#installation-on-microcontroller-boards)
5. [ESP8622: MicroPython](#esp8622-micropython)
6. [ESP8622: Install and Deploy your own App](#esp8622-install-and-deploy-your-own-app)
7. [ESP8622: Using WiFi](#esp8622-using-wifi)
8. [Raspberry Pi Zero W: MicroPython](#raspberry-pi-zero-w-micropython)
8. [Raspberry Pi Zero W: Install and Deploy your own App](#raspberry-pi-zero-w-install-and-deploy-your-own-app)
8. [Raspberry Pi Zero W: Using WiFi](#raspberry-pi-zero-w-using-wifi)

## Documentation

- [Slides](./IoT01Introduction.pdf) from module "IoT Engineering" in [BSc Computer Sciences](https://www.fhnw.ch/en/degree-programmes/engineering/computer-sciences)


## MicroPython

*MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.* -- Quote from the [MicroPython Website](https://micropython.org/)

## Developing with MicroPython

Check the following points:

- Use the **MU-Editor** which can be downloaded from https://codewith.mu/

    Note for Mac Users with Catalina OSX:  
    Start the application for the first time with CTRL Key pressed to be able to accept the security restrictions be the macos. Use version Mu 1.1.0.alpha.2

-  Use a Python3 **Virtual Environment**

    You need full Python on your host machine to be able to run the `esptool` which is needed to bridge the gap between the host machine and the microcontroller.

    Check if `virtualenv` is installed

    ```
    $  which virtualenv/usr/local/bin/virtualenv
    ```

    If no installation can be found, install it using pip:

    ```
    $ pip install virtualenv
    ```

    Use it now to setup a Python3 Virtual Environment:

    ```
    $ virtualenv -p python3 env
    $ source env/bin/activate
    (env) $ python -V
    Python 3.7.6
    (env) $ deactivate
    ```

- The **MicroPython Reference Docs** can be found on https://docs.micropython.org/en/latest/

## Installation on Microcontroller Boards

Here you will information how to install/use MicroPython on the two boards: [ESP8622](https://www.adafruit.com/product/3213) and [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/). The installation and the setup differs, due to the different architectures of the two microcontrollers. While the ESP8266 relies on a computer running Windows, OS X or Linux to obtain programming code, the Raspberry Pi is a separate, small computer usally connected to a monitor via HDMI and controlled by a USB mouse and keyboard. But, if using a Raspberry Pi as embedded controller, a `ssh` connection is usally the preferred way to go.

## ESP8622: MicroPython

Install the firmware as follows:

- Read [Installing MicroPython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro)  from the [Quick reference for the ESP8266](https://docs.micropython.org/en/latest/esp8266/quickref.html#).

- [Get the firmware](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#getting-the-firmware). Choose the latest stable firmware release. It's this firmware which runs the MicroPython applications on the board.

- Identify your USB Port after connecting the ESP8266 to your host computer.  
  On MacOS, it has a name like `/dev/cu.usbserial-01749340`.

- [Deploy the firmware](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware). The firmware must be loaded onto the ESP8622, which is connected over USB to the host. Use the tool `esptool.py`. Example on MacOS:

    ```
    % USB=/dev/cu.usbserial-01749340
    % IMAGE=esp8266-20191220-v1.12.bin
    % esptool.py --port $USB erase_flash
    % esptool.py --port $USB --baud 115200 write_flash --flash_size=detect 0 $IMAGE
    ```

- Read from [Quick reference for the ESP8266](https://docs.micropython.org/en/latest/esp8266/quickref.html#) the chapter [Getting a MicroPython REPL prompt](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html). The term “REPL” is an acronym for *Read*, *Evaluate*, *Print* and *Loop*. It is an interactive way to talk to the computer in Python.

### Running your "Hello World" on ESP8622

Launch your **MU-Editor** and follow the [Start Here!](https://codewith.mu/en/tutorials/1.0/start) tutorial to write and to run your first MicroPython application.

Notes: 
- **REPL**: Use mode "ESP MicroPython". See figure below:

  <img src="mu-mode.png">

## ESP8622: Install and Deploy your own App

Follow these [instructions](blink) to install a *Blink* App permanently on the ESP8622.

## ESP8622: Using WiFi

The ESP8622 has WiFi support on board. There are two WiFi interfaces, one for the station (when the ESP8266 connects to a router) and one for the access point (for other devices to connect to the ESP8266). Check the information on chapter [Network basics](https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html#network-basics) to be able to connect your ESP8622 to a wireless network of your choice.

**NOTES**:
- To use WiFi in your own application, it is important to configure the WiFi network access at boot time.
- Check the [Boot process](https://docs.micropython.org/en/latest/esp8266/general.html#boot-process), especially the roles of the two files `boot.py` and `main.py`.

## Raspberry Pi Zero W: MicroPython

### "Hello World": The first application

## Raspberry Pi Zero W: Install and Deploy your own App

## Raspberry Pi Zero W: Using WiFi
