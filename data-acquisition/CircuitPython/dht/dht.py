import time
import adafruit_dht
import board

# Constants
INTERVAL = 5

# Setup
dht = adafruit_dht.DHT11(board.D9)  # nRF52840, Grove D4
    
# Main Loop
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