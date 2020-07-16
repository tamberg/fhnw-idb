# Using DHT sensor with Python on Raspberry Pi

## Prerequisites

You have successfully completed all steps in [Getting Started](https://github.com/tamberg/fhnw-idb/tree/master/introduction/raspberry#install-and-deploy-your-own-app-as-a-service). That means: 

- You have a running OS on your Raspberry Pi.
- You can connect to your Raspbetty Pi using `ssh` (or an equivalent ssh tool).
- You have python3 installed on your Raspberry Pi.
- You can run the [Blink App](../../introduction/raspberry/blink/README.md).

## DHT sensor in action

This Lab is based on the information found in this [post](https://www.deviceplus.com/raspberry-pi/lets-build-mobile-gadget-using-compact-raspberry-pi-zero-build-environment-check-device-using-grove-sensor/)

### Connecting the DHT sensor to the Raspberry Pi

Connect the DHT sensor to PIN D16 of the Grove Adapter, as shown in figure 1.

<img src="../../docs/raspberry-dht.jpg" width="900" height="450">

Figure 1: DHT sensor connected to PIN 16

### Read the DHT sensor

1. Check that the library `grove.py` is installed on your Raspberry Pi, with:

    ```shell
    $ pip3 show grove.py
    Name: grove.py
    Version: 0.6
    Summary: Python library for Seeedstudio Grove devices
    ...
    ```

2. Download the file [`dht.py`](dht.py) on to your Raspberry Pi.

   This is a small python app using the DHT sensor, which is connected to PIN D16, to read out the temperature and humidity and to print  these values to the console, including a timestamp. 

3. Run the app with

   ```shell
   $ python3 dht.py
   09:19:45,25,53
   ```

   As you can see, the sensor is read just once, but the values are separated by a comma, waht will be the base to create a cvs file for Excel.

### Create Excel file (format csv)

The console output can be redirected into a file, with:

```shell
$ python3 dht.py > dht.csv
```

As described in the [Blink App](../../introduction/raspberry/blink/README.md) the `cron` system tool can be used to scheduke a program at a given interval. 

1. Load on your Raspberry Pi the crontab file into a editor:

   ```shell
   $ crontag -e
   ```

2. Add the following entry:

   ```shell
   * * * * * /usr/bin/python3 /home/pi/dht/dht.py >> /tmp/dht.csv 
   ```

   `cron` will schedule the app `dht.py` each minute and write the console output into file `/tmp/dht.csv`.

3. Save the file

4. `cron` will now run the program each minute. Check if the values are appended to file `dht.csv`.

### Visualize and Analyse the sensor values

1. Copy the file `dht.csv` to your computer and import this file into Excel. Create a diagram to visualize the temperature and humidity. You should get something like shown in figure 2.

   <img src="../../docs/excel.png" width="900" height="450">

   Figure 2: Example of a visualisation in Excel

2. Analyse the data. 

3. **Improve the program, if necessary.** You should have a reasonable output in the end.