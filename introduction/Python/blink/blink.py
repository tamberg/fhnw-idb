import time
from grove.grove_led import GroveLed

# setup
pin = 5 # D5
led = GroveLed(pin)

# main loop
while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)