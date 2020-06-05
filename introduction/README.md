# IoT Introduction

## Documentation

- [Slides](./IoT01Introduction.pdf) from module "IoT Engineering" in [BSc Computer Sciences](https://www.fhnw.ch/en/degree-programmes/engineering/computer-sciences)
- [Slides](./CAS-IoT.pdf) from module "IoT" in [CAS Digital Industry](https://www.fhnw.ch/de/weiterbildung/technik/cas-digital-industry)

## MicroPython

*MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.* -- Quote from the [MicroPython Website](https://micropython.org/)

### Developing with MicroPython

Check the following points:

- Use the **MU-Editor** which can be downloaded from https://codewith.mu/

    Note for Mac User with Catalina OSX:  
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

Notes:

- "Third Party Packages" support within mu-editor does not work under MacOS due to missing SSL/TLS support
  Work-Around:  
  pip install  --target "/Users/luthiger/Library/Application Support/mu/site-packages"

- WiFi support  
    see  https://diyprojects.io/micropython-tutorial-manage-wifi-connection-startup-esp8266-esp32/

- Using WebREPL to download files to the ESP8266 board  
    see https://docs.micropython.org/en/latest/esp32/quickref.html#webrepl-web-browser-interactive-prompt

### Installation on Microcontroller Boards

Here you will information how to install/use MicroPython on the two boards: [ESP8622](https://www.adafruit.com/product/3213) and [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/). The installation and the setup differs completely, due to the different architectures of the two microcontrollers. While the ESP8266 relies on a computer running Windows, OS X or Linux to obtain programming code, the Raspberry Pi is a separate, small computer usally connected to a monitor via HDMI and controlled by a USB mouse and keyboard. But, if using a Raspberry Pi as embedded controller, a `ssh` connection is usally the preferred way to go.

#### ESP8622

The following links are essential:

- from [Quick reference for the ESP8266](https://docs.micropython.org/en/latest/esp8266/quickref.html#) the chapter [Installing MicroPython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro)
- from [Quick reference for the ESP8266](https://docs.micropython.org/en/latest/esp8266/quickref.html#) the chapter [Getting a MicroPython REPL prompt
](https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html)

##### "Hello World": The first application

#### Raspberry Pi Zero W

##### "Hello World": The first application