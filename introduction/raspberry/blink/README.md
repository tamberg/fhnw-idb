# Blink App

## Challenge

The small application in `blink.py` toggles the  grove [LED](https://github.com/tamberg/fhnw-idb/wiki/Grove-Actuators#led) endlessly. But the application is not started again after a reboot.

**Question: How it possible to run own code even after rebooting the Pi?**

## Solution

You will create a stand-alone executable with [PyInstaller](https://www.pyinstaller.org/) and install the executable as a [systemd service](https://www.raspberrypi.org/documentation/linux/usage/systemd.md).

Use the file [blink.py](./blink.py) and follow these steps:

1. Connect the Grove Red LED to GPIO `G5` and powerup the Pi.

2. Copy file `blink.py` onto the Pi using the program `scp`, e.g.:

   ```shell
   $ scp blink.py pi@192.168.0.11:
   ```

   Note: Use the IP-address of your Pi.

3. Open a terminal to the Pi with `ssh`, e.g.

   ```shell
   $ ssh pi@192.168.0.11
   ```

   Note: Use the IP-address of your Pi.

4. Install the library `grove.py` (from Seeed-Studio) on the Pi:

   ```shell
   $ pip3 install grove.py
   ```

4. Start `blink.py` on the Pi:

   ```shell
   $ python3 blink.py
   ```
   **Does it blink?**

To keep running this app, even after a reboot, it must be installed as a systemd service. To be able to run the application as service, the Python application and all its dependencies must be bundled into a single package. The python tool [PyInstaller](https://pyinstaller.readthedocs.io/en/stable/index.html#) can be used for this packaging.

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
   ````

   **Be patient.** This will take some seconds on the first run.

4. Copy distribution `dist` to folder `/usr/local/bin`:

   ```shell
   $ sudo cp -r -r dist/blink /usr/local/bin
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
