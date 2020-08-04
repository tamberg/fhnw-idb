import board
import digitalio
import time

actuator = digitalio.DigitalInOut(board.D5) # nRF52840, Grove D2
actuator.direction = digitalio.Direction.OUTPUT

while True:
    actuator.value = True
    time.sleep(1)
    actuator.value = False
    time.sleep(1)
