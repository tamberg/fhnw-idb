# Blink App

## Challenge

The small application in `blink.py` toggles the  grove [LED](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#led) endlessly. But the application is not started again after a reboot.

**Question: How it possible to run own code even after rebooting the Pi?**

## Solution

You will use the [systemd service](https://www.raspberrypi.org/documentation/linux/usage/systemd.md) and the system command `systemctl` to run the python app even after reboot.

Use the file [blink.py](./blink.py) and follow these steps:

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

4. Install the library `grove.py` (from Seeed-Studio) on the Pi:

   ```shell
   $ pip3 install grove.py
   ```

5. Start `blink.py` on the Pi:

   ```shell
   $ python3 blink.py
   ```
   **Does it blink?**

6. **Or** you can turn on/off the LED manually using python's IDLE:

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

To keep running this app, even after a reboot, it must be installed as a systemd service. You have to options to be able to run the application as service.


**Option 1 (using `systemctl`)**

Use `systemctl` to start the python app as python script. More to find [here](https://www.raspberrypi.org/documentation/linux/usage/systemd.md). 

**Note**: If the app is stateful, it must be run as a service, to be able to keep/store state information between the different calls.

Note:

- If you use print statements in your python app, you can see them using the tool `journalctl` as:

  ```shell
  $ journalctl -f -u blink.service
  ```

**Option 2 (using `cron`)**

Use `cron` to schedule the python application at a given interval. 

**Note**: This is the preferred way if the app is stateless.

Links:

- see [Scheduling tasks with Cron](https://www.raspberrypi.org/documentation/linux/usage/cron.md)
- see [Setting Up A Cron Job On The Raspberry Pi](https://www.bc-robotics.com/tutorials/setting-cron-job-raspberry-pi/)

  **Important**: Use absolute path names for the python interpreter and for your python script within your cron entry

**Option 3 (for experts)**

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

   **Test it!**   