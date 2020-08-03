# Using a DHT sensor with CircuitPython on nRF52840

## Prerequisites

You have successfully completed all steps in [Getting Started](../../introduction/CircuitPython/README.md). That means: 

- You have the MU-Editor installed.
- You the firmware flashed on your ESP8266.
- You can run the [Blink App](../../introduction/CircuitPython/blink/README.md).

## DHT sensor in action

This Lab is based on the information found in

- the [DHT MicroPython Docs](https://docs.micropython.org/en/latest/esp32/quickref.html#dht-driver)

### Connecting the DHT sensor to the ESP8266 board

Connect the DHT sensor to PIN D2 of the Grove Adapter, as shown in figure 1.

<img src="esp8266-dht.jpg" width="640">

Figure 1: DHT sensor connected to PIN D2

### Read the DHT sensor

1. Open your MU-Editor and connect your ESP8266 over USB.

2. Load the file [`dht.py`](dht.py) into your MU-Editor.

   This is a small python app  using the DHT sensor, which is connected to PIN D2, to read out the temperature and humidity and to print  these values to the console, including a timestamp. 

3. Run the app (see figure 2).

   <img src="esp8266-mu-editor.jpg" width="640">

   Figure 2: App `dht.py` in action

   The values are printed out to the console.

### Create Excel file (format csv)

The console output can be copied and pasted into a excel file.

1. Open a new text file.

2. Create the column header with `Time,Temp,Hum`.

2. Copy and paste the values from the console into the text file. Separate the columns with a comma.

3. Save the file as `dht.csv`.


### Visualize and Analyse the sensor values

**Visualize**

Using Jupyter notebook (Option 1):

1. Open the given Jupyter notebook [`dht.ipynb`](./dht.ipynb).

2. Check the filename of the csv-file, which is loaded into the notebook.

3. Run the notebook. You should get something, as shown in figure 3.

   <img src="esp8266-jupyter.png" width="640">

   Figure 3: Example of a visualisation in Jupyter notebook

Using Excel (Option 2):

1. Create a diagram to visualize the temperature and humidity. You should get something, as shown in figure 4:

   <img src="esp8266-excel.png" width="640">

   Figure 4: Example of a visualisation in Excel

**Analyse**

Analyse the data for wrong or missing values. It can happen! The sensor is cheap! **Improve the program, if necessary.** You should have a reasonable output in the end.
