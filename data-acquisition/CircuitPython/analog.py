import analogio
import board
import time

sensor = analogio.AnalogIn(board.A0) # nRF52840 A0, Grove A0

while True:
    value = sensor.value
    voltage = (value * 3.3) / 65536
    print((value, voltage)) # serial plotter format
    time.sleep(0.1)
