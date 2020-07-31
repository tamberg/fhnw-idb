import board
import digitalio
import time

button = digitalio.DigitalInOut(board.D9) # nRF52840, Grove D4
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    print(button.value)
    time.sleep(0.1)
