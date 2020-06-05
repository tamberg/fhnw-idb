import time
import sys
import json
import Adafruit_DHT as dht
import paho.mqtt.client as mqtt
from grove.grove_led import GroveLed

LED_PIN = 5 # D5
DHT_PIN = 16 # D16
THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN = "uIAy5Iw2x92e1SydrwLN"
INTERVAL = 5

def connect_thingsboard():
    client = mqtt.Client()
    client.username_pw_set(ACCESS_TOKEN)

    # Connect to ThingsBoard
    client.connect(THINGSBOARD_HOST, 1883, 60)
    client.loop_start()
    return client

def connect_sensor():
    sensor = dht.DHT11
    return sensor

def connect_led():
    return GroveLed(LED_PIN)

def pulse_led(led):
    led.on()
    time.sleep(0.1)
    led.off()


def main():
    client = connect_thingsboard()
    sensor = connect_sensor()
    led = connect_led()

    next_reading = time.time()
    telemetry = {'timestamp': time.time(), 'temperature': 0, 'humidity': 0}

    try:
        # Go into endless loop
        while True:
            # Make a measurement 
            humidity, temperature = dht.read_retry(sensor, DHT_PIN)

            # Wait
            next_reading += INTERVAL
            sleep_time = next_reading - time.time()
            if sleep_time > 0:
                time.sleep(sleep_time)

            # Print the sensor values to the console
            if humidity is not None and temperature is not None:
                now = time.time()
                humidity = round(humidity, 2)
                temperature = round(temperature, 2)
                t = time.localtime(now)
                print("t={:02d}:{:02d}:{:02d} temp={:g}C humidity={:g}%".format(t.tm_hour, t.tm_min, t.tm_sec, temperature, humidity))

                # Format measurement as json object
                telemetry['timestamp'] = now
                telemetry['temperature'] = temperature
                telemetry['humidity'] = humidity
            
                # Publish measurement as MQTT message (without checking the delivery status)
                client.publish("v1/devices/me/telemetry", json.dumps(telemetry))

                # LED
                pulse_led(led)
   
            else:
                print("Sensor failure. Check wiring.")
                sys.exit()
    except KeyboardInterrupt:
        pass

    # Disconnect from ThingsBoard
    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    main()