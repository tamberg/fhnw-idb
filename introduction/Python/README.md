# Getting Started with Python on Raspberry Pi

1. [Prerequisites](#prerequisites)
2. [Install Python 3](#install-python-3)
3. [Install Grove](#install-grove)
4. [Install Blinka](#install-blinka)
5. [Run your first program](#run-your-first-program)

## Prerequisites
The following steps require a Raspberry Pi Zero W with Raspberry Pi OS Lite, a Linux operating system. To install it, see [Raspberry Pi Zero W Setup](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#setup). Make sure to [configure Wi-Fi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#configure-wi-fi) and [enable SSH access](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#enable-ssh) so you can [find your Pi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#find-your-pi), if your computer is in the same local Wi-Fi network.

## Install Python 3
A fresh installation of the Raspberry Pi OS Lite has Python 3 preinstalled. Check this with:

```shell
$ python --version
Python 3.9.2
```

If you don't have Python3 installed, install it with:
```shell
$ sudo apt update
$ sudo apt install python3
````

Additionally, you need `pip3` to add python packages to your project. Install `pip3` as follows:
```shell
$ sudo apt-get install python3-pip
$ pip --version
pip 20.3.4 from /usr/lib/python3/dist-packages/pip (python 3.9)
```

The [python documentation](https://www.raspberrypi.org/documentation/usage/python/) includes chapters on [installing libraries](https://www.raspberrypi.com/documentation/computers/os.html#installing-python-libraries) and using [GPIO in Python](https://www.raspberrypi.org/documentation/usage/gpio/python/README.md).

## Install Grove
To access the GPIOs on the Pi and work with Grove sensors and actuators we use the [Grove Python package](https://github.com/Seeed-Studio/grove.py).

Install the Grove Python package with:

```shell
$ sudo pip install grove.py
```

Here are some [code examples](https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md#gui-graphical-user-interface) by Seeed Studio.

## Install Blinka
As an alternative to Grove and for additional sensor libraries we use the [Blinka Python package](https://github.com/adafruit/Adafruit_Blinka).

Install the Blinka Python package with the following steps, based on [this tutorial](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi) by Adafruit:

```
$ sudo raspi-config # Advanced options > Expand file system
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo pip install --upgrade setuptools
$ sudo pip install --upgrade adafruit-python-shell
$ wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
$ sudo python3 raspi-blinka.py
```

## Run your first program

Now, [run your first program](blink_grove/README.md) and install it permanently on your microcontroller.
