import time
import board
import pulseio

led = pulseio.PWMOut(board.A0, frequency=5000, duty_cycle=0)

while True:
    for i in range(100):
        value = int(i * 65535 / 100)
        led.duty_cycle = value
        time.sleep(0.01)
