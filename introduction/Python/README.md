# Getting Started with Python on Raspberry Pi

1. [Prerequisites](#prerequisites)
2. [Install Python 3](#install-python-3)
3. [Install Grove](#install-grove)
4. [Install Blinka](#install-blinka)
5. [Run your first program](#run-your-first-program)

## Prerequisites
The following steps require a Raspberry Pi Zero W with Raspberry Pi OS Lite, a Linux operating system. To install it, see [Raspberry Pi Zero W Setup](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#setup). Make sure to [configure Wi-Fi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#configure-wi-fi) and [enable SSH access](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#enable-ssh) so you can [find your Pi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#find-your-pi), if your computer is in the same local Wi-Fi network.

## Install Python 3
A fresh installation of the Raspberry Pi OS Lite has Python 2 preinstalled. Check it on your Pi with:

```shell
$ python --version
Python 2.7.16
```

Check if python3 and pip3 are installed. Otherwise install them with:
```shell
$ sudo apt update
$ sudo apt install python3
$ sudo apt-get install python3-pip
$ python3 --version
Python 3.7.3
$ pip3 --version
pip 18.1 from /usr/lib/python3/dist-packages/pip (python 3.7)
```

Check the [python documentation](https://www.raspberrypi.org/documentation/usage/python/) on raspberry.org. Following chaptes are important:

- Installing Python libraries
- [GPIO in Python](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md)

## Install Grove
To access the GPIOs on the Pi and work with Grove sensors and actuators we use the Grove Python package [grove.py](https://github.com/Seeed-Studio/grove.py).

Install the Grove Python package with:

```shell
$ sudo pip3 install grove.py
```

Checkout these [demos and code examples](https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md#gui-graphical-user-interface) from Seeed-Studio.

## Install Blinka
Based on https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

```
$ sudo raspi-config # Advanced options > Expand file system

$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3-pip
$ sudo pip3 install --upgrade setuptools

$ sudo pip3 install --upgrade adafruit-python-shell
$ wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
$ sudo python3 raspi-blinka.py
$ python --version
Python 3.7.3
$ rm raspi-blinka.py

$ nano /boot/config.txt
  # add this line to the bottom
  dtoverlay=spi1-3cs
$ ls /dev/i2c* /dev/spi*

$ pip3 install --upgrade adafruit_blinka
```

## Run your first program

Follow these steps to [run your first program](blink_grove/README.md) and install it permanently on your microcontroller.
