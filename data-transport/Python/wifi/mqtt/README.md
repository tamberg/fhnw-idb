# Publish Data using the MQTT API
How to write simple test data using ThingSpeak's MQTT API of ThingSpeak.

We will use for our examples the [Eclipse Paho Python](https://github.com/eclipse/paho.mqtt.python#publishing) library to publish MQTT messages.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB or ssh.
* Copy the content of [thingspeak_mqtt.py](thingspeak_mqtt.py) to your Pi.
* Install the Eclipse Paho library with `pip3 install paho-mqtt`
* Update `channelID` and `writeAPIKey` with your keys.
* Run example from the command line with `python3 thingspeak_mqtt.py`

## Hardware
* [Raspberry Pi Zero W](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W) controller.
