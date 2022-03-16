import time
import math
# check, that python lib 'grove' is installed; pip3 freeze | grep grove
import grove.grove_temperature_humidity_sensor as dht

DHT_PIN = 16 # rasperry pi Pin16, Grove D16


def setup():
    sensor = dht.DHT("11", DHT_PIN)
    return sensor


def main():
    # Initialize
    sensor = setup()

    try:
        # Try to grab a sensor reading
        humidity, temperature = sensor.read()
        
        # Print the sensor values
        now = time.time()
        t = time.localtime(now)
        humidity = int(round(humidity))
        temperature = int(round(temperature))
        if math.isnan(temperature) == False and math.isnan(humidity) == False:
            print("{:02d}:{:02d}:{:02d},{:g},{:g}".format(t.tm_hour, t.tm_min, t.tm_sec, temperature, humidity), flush=True)
    except IOError:
        pass

if __name__ == '__main__':
    main()