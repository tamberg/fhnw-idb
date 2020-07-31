import dht
import utime
import machine

# Use D2 on Grove Adapter => Pin 2
sensor = dht.DHT11(machine.Pin(2))

# Attention!
# Set date and time (year,month,day,0,hour,min,sec,0)
machine.RTC().datetime((2020,7,16,0,12,35,0,0))
rtc = machine.RTC()

while True:
    # Take a measurement
    sensor.measure()

    # Print the sensor values
    t = utime.localtime(utime.time())
    humidity = int(round(sensor.humidity()))
    temperature = int(round(sensor.temperature()))
    print("{:02d}:{:02d}:{:02d},{:g},{:g}".format(t[3], t[4], t[5], temperature, humidity))

    utime.sleep(15)
