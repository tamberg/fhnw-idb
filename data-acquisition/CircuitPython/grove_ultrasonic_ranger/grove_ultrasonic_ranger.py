# Based on https://raw.githubusercontent.com/Seeed-Studio/grove.py/master/grove/grove_ultrasonic_ranger.py licensed under MIT License

#import sys
#from grove.gpio import GPIO
import board
import digitalio
import time

_SENSOR_PIN = board.D5 # nRF5840 D5, Grove D2
_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        #self.dio = GPIO(pin)
        self.dio = digitalio.DigitalInOut(pin)

    def _get_distance(self):
        #self.dio.dir(GPIO.OUT)
        self.dio.direction = digitalio.Direction.OUTPUT
        #self.dio.write(0)
        self.dio.value = False
        time.sleep(0.000002)
        #self.dio.write(1)
        self.dio.value = True
        time.sleep(0.000010)
        #self.dio.write(0)
        self.dio.value = False

        #self.dio.dir(GPIO.IN)
        self.dio.direction = digitalio.Direction.INPUT

        #t0 = time.time()
        t0 = time.monotonic()
        count = 0
        while count < _TIMEOUT1:
            #if self.dio.read():
            if self.dio.value == True:
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        #t1 = time.time()
        t1 = time.monotonic()
        count = 0
        while count < _TIMEOUT2:
            #if not self.dio.read():
            if self.dio.value == False:
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        #t2 = time.time()
        t2 = time.monotonic()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist

if __name__ == '__main__':
    sonar = GroveUltrasonicRanger(_SENSOR_PIN)

    print('Detecting distance...')
    while True:
        print('{} cm'.format(sonar.get_distance()))
        time.sleep(1)
