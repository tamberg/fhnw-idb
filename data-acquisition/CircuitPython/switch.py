import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D5) # nRF52840, Grove D2
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.D9) # nRF52840, Grove D4
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP

while True:
    led.value = button.value
    time.sleep(0.1)
