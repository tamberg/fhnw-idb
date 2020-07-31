# Using a DHT sensor with Python on Raspberry Pi

## Prerequisites

You have successfully completed all steps in [Getting Started](../../introduction/raspberry/README.md). That means: 

- You have a running OS on your Raspberry Pi.
- You can connect to your Raspberry Pi using `ssh` (or an equivalent ssh tool).
- You have python3 installed on your Raspberry Pi.
- You can run the [Blink App](../../introduction/raspberry/blink/README.md).

## DHT sensor in action

This Lab is based on the information found in

- the [SEEED Docs](https://github.com/Seeed-Studio/grove.py/tree/master/doc#temperature--humidity-sensordht11)

- this [post](https://www.deviceplus.com/raspberry-pi/lets-build-mobile-gadget-using-compact-raspberry-pi-zero-build-environment-check-device-using-grove-sensor/)

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

   As you can see, the sensor is read just once, but the values are separated by a comma, what will be the base to create a cvs file for Excel.

### Create Excel file (format csv)

The console output can be redirected into a file, with:

```shell
$ python3 dht.py > dht.csv
```

As described in the [Blink App](../../introduction/raspberry/blink/README.md) the `cron` system tool can be used to schedule a program at a given interval. 

1. On your Raspberry Pi load the crontab file into a editor:

   ```shell
   $ crontag -e
   ```

2. Add the following entry:

   ```shell
   * * * * * /usr/bin/python3 /home/pi/dht/dht.py >> /tmp/dht.csv 
   ```

   Adding this entry, `cron` will schedule the app `dht.py` each minute and append the console output to file `/tmp/dht.csv`.

   **Note**: 

   - The path entries must match your setuo!

3. Save the file.

4. `cron` will now run the program each minute. Check if the values are appended to file `dht.csv`.

### Visualize and Analyse the sensor values

1. Copy the file `dht.csv` to your computer and import this file into Excel. 

2. Create a diagram to visualize the temperature and humidity. You should get something like shown in figure 2.

   <img src="../../docs/excel.png" width="900" height="450">

   Figure 2: Example of a visualisation in Excel

3. Analyse the data for wrong or missing values. It can happen! The sensor is cheap!

4. **Improve the program, if necessary.** You should have a reasonable output in the end.

#### Option

Use a Jupyter notebook.
