import time
import board
import pulseio

cycle = 65535 // 5 # 20% power
buzzer = pulseio.PWMOut(board.A0,
  duty_cycle=cycle, variable_frequency=True)

while True:
    for f in (262, 294, 330, 392):
        buzzer.frequency = f
        time.sleep(0.1)

