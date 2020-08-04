import board
import digitalio
import time

sensor = digitalio.DigitalInOut(board.D9) # nRF52840, Grove D4
sensor.direction = digitalio.Direction.INPUT
sensor.pull = digitalio.Pull.UP

while True:
    print(sensor.value)
    time.sleep(0.1)
