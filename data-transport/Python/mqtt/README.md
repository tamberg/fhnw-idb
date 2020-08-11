# Pubish Data using the MQTT API
How to write simple test data using ThingSpeak's MQTT API of ThingSpeak.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB.
* Copy the content of [ts_mqtt.py](ts_mqtt.py) to your Pi.
* Install the Eclipse Paho library with `pip3 install paho-mqtt`
* Update `writeAPIKey` with your *Write API Key*.
* Run example from the command line with `python3 ts_mqtt.py`

## Hardware
* [Raspberry Pi Zero W](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W) controller.
