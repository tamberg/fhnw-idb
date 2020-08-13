import board
import time
import tm1637lib

display = tm1637lib.Grove4DigitDisplay(board.D9, board.D10) # nRF52840 D9, D10, Grove D4

colon = True
while True:
    display.show("0000")
    display.set_colon(colon)
    colon = not colon
    time.sleep(1)
