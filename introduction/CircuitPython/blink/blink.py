import board
import digitalio
import time

def do_blink():
  led = digitalio.DigitalInOut(board.RED_LED)  # general-purpose RED LED on Pin D3
  led.direction = digitalio.Direction.OUTPUT

  while True:
      led.value = True
      time.sleep(1)
      led.value = False
      time.sleep(1)