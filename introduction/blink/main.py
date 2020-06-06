from machine import Pin
import time

led = Pin(0, Pin.OUT)    # create output pin on GPIO0
val = True

while True:
    led.value(val)
    val = not val   # toggle pin
    time.sleep_ms(100)
