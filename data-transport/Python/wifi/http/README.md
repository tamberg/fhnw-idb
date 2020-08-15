# Write Data using the REST API
How to write simple test data using ThingSpeak's REST API of ThingSpeak.

We will use for our examples the module [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) to send simple HTTP GET requests.

## Running the example
* Set up the [hardware](#Hardware), connect it to your computer via USB or ssh.
* Copy the content of [thingspeak_http.py](thingspeak_http.py) to your Pi.
* Update `writeAPIKey` with your *Write API Key*.
* Run example from the command line with `python3 thingspeak_http.py`

## Hardware
* [Raspberry Pi Zero W](https://github.com/tamberg/fhnw-idb/wiki/Raspberry-Pi-Zero-W) controller.