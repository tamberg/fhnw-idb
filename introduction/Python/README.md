# Getting Started with Python on Raspberry Pi

1. [Prerequisites](#prerequisites)
2. [Python](#python)
3. [Install and Deploy your own Program](#install-and-deploy-your-own-program)

## Prerequisites

It is necessary to install a Raspberry Pi operation system, which is Linux-based, on your Pi. There exist several resources explaining this procedure. Read our Wiki Page [Setup on a Raspberry Pi Zero W](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#setup)

**Important**: 
- Choose **Raspberry Pi OS Lite**. The Raspberry Pi Zero W has limited computing resources. Desktop software and applications like office application are not needed.
- Check that `wifi` and `ssh` are enabled and can be used without problems. You have to be with your computer and with your Pi on the same network!

  See [Configure Wi-Fi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#configure-wi-fi) and [Enable SSH
](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#enable-ssh).
- Find the **IP address of your Pi** using the information in the [Find your Pi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#find-your-pi).  
Use the commands `ifconfig` or `ipconfig` and `nmap`.

## Python

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


## Install GPIO python package

To access the GPIOs on the Pi you need to install correspondig packages. 
[grove.py](https://github.com/Seeed-Studio/grove.py) is such a Python package for Seeedstudio Grove Devices, especially good on Rapsberry Pis. 

Install it with:

```shell
$ sudo pip3 install grove.py
```

Checkout these [demos and code examples](https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md#gui-graphical-user-interface) from Seed-Studio.

## Run your first program

Follow these steps to [run your first program](blink_grove/README.md) and install it permanently on your microcontroller.
