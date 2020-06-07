# Introduction to IoT
1. [Documentation](#documentation)
2. [Python vs. MicroPython](#python-vs.-micropython)
3. [Getting Started with MicroPython on ESP8266](esp8266)
4. [Getting Started with MicroPython on Raspberry Pi](raspberry)

## Documentation

- [Slides](./IoT01Introduction.pdf) from module "IoT Engineering" in [BSc Computer Sciences](https://www.fhnw.ch/en/degree-programmes/engineering/computer-sciences)


## Python vs. MicroPython

> Finally, Python had moved off of desktops and servers and into the world of sensors, actuators, motors, LCD displays, buttons, and circuits. While this presented many challenges, there were also copious opportunities. Desktop and server hardware requires gigahertz processors, gigabytes of RAM, and terabytes of storage. They also need fully-fledged operating systems, device drivers, and true multitasking.
>
> In the microcontroller world, however, MicroPython is the operating system.

— Quote from [MicroPython: An Intro to Programming Hardware in Python](https://realpython.com/micropython/)

> MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

— Quote from the [MicroPython Website](https://micropython.org/)

### Developing with MicroPython

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