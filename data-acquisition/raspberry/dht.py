import time
# check, that python lib 'grove' is installed; pip3 freeze | grep grove
import grove.grove_temperature_humidity_sensor as dht

DHT_PIN = 16 # D16


def connect_sensor():
    sensor = dht.DHT("11", DHT_PIN)
    return sensor


def main():
    # Initialize
    sensor = connect_sensor()

    try:
        # Try to grab a sensor reading
        humidity, temperature = sensor.read()
        
        # Print the sensor values
        now = time.time()
        t = time.localtime(now)
        humidity = int(round(humidity))
        temperature = int(round(temperature))
        print("{:02d}:{:02d}:{:02d},{:g},{:g}".format(t.tm_hour, t.tm_min, t.tm_sec, temperature, humidity), flush=True)

    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()