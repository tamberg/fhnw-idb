import board
import digitalio
import time

# setup
led = digitalio.DigitalInOut(board.D5)  # LED on Pi Zero W, Grove D5
led.direction = digitalio.Direction.OUTPUT

# main loop
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)
