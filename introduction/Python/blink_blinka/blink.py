import board
import digitalio
import time

# setup
led = digitalio.DigitalInOut(board.D5)  # Pi Zero W, Grove D5
led.direction = digitalio.Direction.OUTPUT

# main loop
while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
