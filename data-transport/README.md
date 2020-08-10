# Data Transport

1. [Overview](#overview)
2. [Resources](#resources)

## Overview
<table><tr><td><img width="600" src="overview-data-transport.png"></td></tr></table>

>Data transport (data transmission, also data communication or digital communications) is the transfer of data (a digital bitstream or a digitized analog signal) over a point-to-point or point-to-multipoint communication channel. 

--- from Wikipedia

To transer the data, a communication channel must be established betwenn the "Connected device" and a "Cloud Backend".

We will use examples of data transport technologies to find out:

* how to established a communication channel between two communication partners?
* how the sensors values can be transfered to the backend?
* how transfer protocols of the internet can be used to simplify the transfer?
* how these transfer protocols differs?

## Resources

- Slides on [Sending Sensor Data to IoT Platforms](http://www.tamberg.org/fhnw/2020/hs/IdbSensorDataPlatforms.pdf).
- Slides on [XYZ](http://www.tamberg.org/fhnw/2020/hs/IdbXYZ.pdf).
- Slides on [XYZ](http://www.tamberg.org/fhnw/2020/hs/IdbXYZ.pdf).
- Slides on [XYZ](http://www.tamberg.org/fhnw/2020/hs/IdbXYZ.pdf).
- Slides on [XYZ](http://www.tamberg.org/fhnw/2020/hs/IdbXYZ.pdf).

## Connecting to Wi-Fi

## ThingSpeak IoT platform

We will use the [ThingSpeak](https://thingspeak.com/) as our *Cloud Backend*. ThingSpeak is an IoT analytics platform service that allows you to aggregate, visualize, and analyze live data streams in the cloud. 

For an introduction look at this tutorial:

* [Introduction to ThingSpeak](https://ch.mathworks.com/de/support/search.html/videos/introduction-to-thingspeak-107749.html?q=&fq=asset_type_name:video%20category:matlab/data-import-and-export&page=1)

Your steps to get started with ThingSpeak are:

1. **Create a free account**
    
    ThingSpeak does provide free access, but with [limited resources and functionality](https://thingspeak.com/prices/thingspeak_student). To use [ThingSpeak](https://thingspeak.com/), start creating a free account with your **FHNW email address** by clicking the button as shown in figure 1.

    <img width="640" src="thingspeak-get-started.png"></td></tr></table>

    Figure 1: Get started on ThingSpeak with a free, limited account

2. **Create a channel**
    
    To be able to collect data on ThingSpeak, you have to provide a so-called **Channel**. Use the information in [Collect Data in a New Channel](https://ch.mathworks.com/help/thingspeak/collect-data-in-a-new-channel.html) to setup your first channel with 3 fields: *Temperature, Humidity, Dew Point*

    Save the channel.

3. **Get your access keys**

    API keys enable you to write data to a channel or read data from a private channel. API keys are auto-generated when you create a new channel.

    You can access your API key ionn your channel page in tab **API Keys**. You will need the **Write API Key**

4. **Test your channel**

    You can test your channel by sending test data manually using the HTTP protocol. Use your browser to do a HTTP GET request as follows:
    
    ```
    https://api.thingspeak.com/update?api_key=<YOUR WRITE API KEY>&field1=0&field2=10&field3=20
    ```

    You should see on each chart one red point, which corresponds to your test values as shown in figure 2.

    <img width="640" src="thingspeak-charts.png"></td></tr></table>

    Figure 2: Charts with first test data

**Your ThingSpeak channel is now ready to collect your sensor data.**

## HTTP Client
ThingSpeak

## MQTT Client
ThingSpeak

## LoRaWAN

## CircuitPython examples
Try these examples with CircuitPython on the nRF52840.

### Wi-Fi
* [Scanning Wi-Fi networks](CircuitPython/wifi_scan)
* [Connecting to a Wi-Fi network](CircuitPython/wifi_connect)
* [Reading the Wi-Fi module MAC address](CircuitPython/wifi_address)

### LoRaWAN
> TODO

## Python examples
Try these examples with Python on the Raspberry Pi.

### Wi-Fi
> TODO
