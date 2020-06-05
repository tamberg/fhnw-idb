import sys
import dht
import network
import utime
import json
import time
from umqtt.simple import MQTTClient
from machine import Pin

def connect_thingsboard():
    # Connect to ThingsBoard
    client = MQTTClient("mqtt_client", "demo.thingsboard.io", user="uIAy5Iw2x92e1SydrwLN", password="", port=1883)
    try:
        client.connect()
        return client
    except OSError:
        print('Failed to connect to ThingsBoard')
        sys.exit()

def test_wlan():
    # Test WLAN connection
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('WLAN not connected')
        sys.exit()

def connect_sensor():
    # use D2 on Grove Adapter => Pin 2
    sensor = dht.DHT11(Pin(2))
    return sensor

def main():
    test_wlan()
    client = connect_thingsboard()
    sensor = connect_sensor()

    # Go into endless loop
    while True:
        # Make a measurement 
        sensor.measure()

        # Print the sensor values to the console
        print("({0:5.1f},{0:5.1f})".format(sensor.temperature(), sensor.humidity()))

        # Format measurement as json object
        telemetry = {"timestamp": utime.time(), "temperature": sensor.temperature(), "humidity": sensor.humidity()}
        
        # Publish measurement as MQTT message (without checking the delivery status)
        client.publish("v1/devices/me/telemetry", json.dumps(telemetry))

        # Wait one second
        time.sleep(1)

    # Disconnect from ThingsBoard
    client.disconnect()

if __name__ == '__main__':
    main()
