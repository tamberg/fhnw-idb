import time
import rtc
import digitalio
import adafruit_dht
import board

INTERVAL = 15


def setup():
    # set the time manually, we are not using a real time clock!
    now = time.struct_time((2020, 8, 3, 18, 14, 0, 1, -1, -1))
    r = rtc.RTC()
    r.datetime = now

    # D5 => Pin D2 on Grove Board; see https://github.com/tamberg/fhnw-idb/wiki/Grove-Adapters#mapping
    dht = adafruit_dht.DHT11(board.D5)
    return dht
    
def measure():
    dht = setup()
    
    while True:
        start = time.time()
        t = time.localtime(start)
        try:
            # Read the temperature and convert it to integer
            temperature = int(round(dht.temperature))
            # Read the humidity and convert it to integer
            humidity = int(round(dht.humidity))
            # Print timestamp, temperatur, humidity
            print("{:d}:{:02d}:{:02d},{:g},{:g}".format(
                t.tm_hour, t.tm_min, t.tm_sec, temperature, humidity))

        except RuntimeError as e:
            # Reading doesn't always work! Just print error and we'll try again
            print("{:d}:{:02d}:{:02d},{:g},{:g}".format(
                t.tm_hour, t.tm_min, t.tm_sec, -1, -1))

        end = time.time()
        # Wait for the remaining time
        time.sleep(INTERVAL - (end - start))