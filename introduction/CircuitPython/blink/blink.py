import board
import digitalio
import time

# setup 
led = digitalio.DigitalInOut(board.RED_LED)  # general-purpose RED LED on Pin D3
led.direction = digitalio.Direction.OUTPUT

# main loop
while True:
    led.value = True
    time.sleep(1)
    led.value = False
    time.sleep(1)