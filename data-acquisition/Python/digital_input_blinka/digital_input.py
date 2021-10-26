import board
import digitalio
import time

sensor = digitalio.DigitalInOut(board.D5) # Pi Zero W, Grove D5
sensor.direction = digitalio.Direction.INPUT
sensor.pull = digitalio.Pull.UP

while True:
    print(sensor.value)
    time.sleep(0.1)
