import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D5) # nRF52840, Grove D2
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)

