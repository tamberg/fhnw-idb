import time
from grove.adc import ADC

adc = ADC()

while True:
    value = adc.read_voltage(4); # Grove A4
    print(value)
    time.sleep(0.1)
