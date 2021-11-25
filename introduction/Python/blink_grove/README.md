# Blink

## Hardware
* [Raspberry Pi Zero W](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W) controller.
* [Grove Base Hat for Raspberry Pi](https://github.com/tamberg/fhnw-idb/wiki/Grove-Adapters#grove-base-hat-for-raspberry-pi) to connect sensors.
* [Grove Red LED](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#led) wired to Grove _D5_ (see figure 1).

<table><tr><td><img width="640" src="setup.jpg"></td></tr></table>

Figure 1: The LED is connected to Pin `D5`.

## Intro

The first, small program toggles the Grove Red LED endlessly. It is based on this [Seeed-Studio example](https://github.com/Seeed-Studio/grove.py/blob/master/doc/README.md#grove---led).

## Question

The small program runs endlessly. But it is not started again after a reboot pf the Pi. That could be a problem for an embedded device, which is not accessible easily.

**Question: How it possible to run own code even after rebooting the Pi?**

## Solution

You will use the [systemd service](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) and the system command `systemctl` to run the python program even after reboot.

Use the file [blink.py](./blink.py) (or the Blinka version [blink.py](./blink.py)) and follow these steps:

1. Connect the Grove Red LED to GPIO `G5` and powerup the Pi.

2. Copy file `blink.py` onto the Pi using the program `scp`, e.g.:

   ```shell
   $ scp blink.py pi@192.168.0.11:
   ```

   **Note**: Use the IP-address of your Pi (see [Find your Pi](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W#find-your-pi)).

3. Open a terminal to the Pi with `ssh`, e.g.

   ```shell
   $ ssh pi@192.168.0.11
   ```

   Note: Use the IP-address of your Pi.

4. Check that the package `grove.py` (from Seeed-Studio) is already installed:

   ```shell
   $ pip3 show grove.py
   ```

5. Start `blink.py` on the Pi:

   ```shell
   $ python3 blink.py
   ```
   **Does it blink?**

6. **Or** you can turn on/off the LED manually using python's IDLE/REPL:

   ```shell
   $ python3
   Python 3.7.3 (default, Dec 20 2019, 18:57:59) 
   [GCC 8.3.0] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>> from grove.grove_led import GroveLed
   >>> led = GroveLed(5)
   >>> led.on()
   >>> led.off()
   >>> led.on()
   >>> led.off()
   >>>
   ```


**Use `systemctl`**

To keep running this program, even after a reboot, it must be installed as a systemd service. Use `systemctl` and  the service file [blink.service](blink.service) to start the python program as system service. Follow these [instructions](https://www.raspberrypi.com/documentation/computers/using_linux.html#the-systemd-daemon) to install the program as a service. 

Note:

- If you use print statements in your python program, you can see them using the tool `journalctl`:

  ```shell
  $ journalctl -f -u blink.service
  ```

<!-- **Optional: Use `cron`**

Use `cron` to schedule the python program at a given interval. You have to change `blink,py` to:

```python
import time
from grove.grove_led import GroveLed

# setup
pin = 5 # D5
led = GroveLed(pin)

# main task
led.on()
time.sleep(0.5)
led.off()
time.sleep(0.5)
```

Links:

- see [Scheduling tasks with Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md)
- see [Setting Up A Cron Job On The Raspberry Pi](https://www.bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/)

  **Important**: Use absolute path names for the python interpreter and for your python script within your cron entry -->

<!-- **Option 3 (optional and for experts)**

Use `systemctl` to start an executable, generate from the python application.

The python app and all its dependencies can be bundled into a single package/executable using the python tool [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html#).

1. Start installing `pyinstaller` **on the Pi** with:

   ```shell
   $ pip3 install pyinstaller
   $ pyinstaller --version
   ```

2. Add python script path `/home/pi/.local/bin` to your PATH variable:

   ```shell
   $ export PATH=$PATH:/home/pi/.local/bin
   ```

3. Run the installer from the folder with file `blink.py` :

   ```shell
   $ PYTHONOPTIMIZE=1 pyinstaller blink.py
   ```

   **Notes:** 
   - This will take some seconds on the first run.
   - When a module is using hidden imports, e.g. `Adafruit_DHT` then these imports must be added on the command line:

      ```shell
      $ PYTHONOPTIMIZE=1 pyinstaller --hidden-import=Adafruit_DHT blink.py
      ```

4. Copy distribution `dist` to folder `/usr/local/bin`:

   ```shell
   $ sudo cp -r dist/blink /usr/local/bin
   ```

5. Copy file `blink.service` onto the Pi using the program `scp`, e.g.:

   ```shell
   $ scp blink.service pi@192.168.0.11:
   ```

6. Copy the service file [blink.service](./blink.service) to folder `/etc/systemd/system`:

   ```shell
   $ sudo cp blink.service /etc/systemd/system/blink.service
   ```

7. Start/stop the service:

   ```shell
   $ sudo systemctl start blink.service
   ```

      ```shell
   $ sudo systemctl stop blink.service
   ```

8. Have it start automatically on reboot:

   ```shell
   $ sudo systemctl enable blink.service
   ```

   **Test it!**    -->
