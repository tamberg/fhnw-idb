import board
import digitalio
import time

actuator = digitalio.DigitalInOut(board.D5)  # Actuator on Pi Zero W, Grove D5
actuator.direction = digitalio.Direction.OUTPUT

while True:
    actuator.value = True
    time.sleep(0.5)
    actuator.value = False
    time.sleep(0.5)