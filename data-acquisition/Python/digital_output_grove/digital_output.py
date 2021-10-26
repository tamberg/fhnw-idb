import time
from grove.gpio import GPIO

actuator = GPIO(5, GPIO.OUT) # Actuator on Pi Zero W, Grove D5

while True:
    actuator.write(True)
    time.sleep(0.5)
    actuator.write(False)
    time.sleep(0.5)
