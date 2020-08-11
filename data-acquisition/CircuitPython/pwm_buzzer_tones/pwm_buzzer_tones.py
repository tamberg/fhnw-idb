import time
import board
import pulseio

cycle = 65535 // 2 # on 50%
buzzer = pulseio.PWMOut(board.A0,
  duty_cycle=cycle, variable_frequency=True)

while True:
    for f in (262, 294, 330, 349, 392):
        buzzer.frequency = f
        time.sleep(0.25)
