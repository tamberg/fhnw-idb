# Based on https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa licensed under LGPL (!)

import time
import board
import busio
import digitalio
from adafruit_tinylora import adafruit_tinylora

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# FeatherWing RFM95, nRF52840
cs = digitalio.DigitalInOut(board.D5)
irq = digitalio.DigitalInOut(board.D10)
rst = digitalio.DigitalInOut(board.D6)

# TODO: App > Device > Settings (ABP) from
# TTN https://console.thethingsnetwork.org/
ttn_dev_address_msb = bytearray([0x00, 0x00, 0x00, 0x00])

ttn_net_session_key_msb = bytearray(
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

ttn_app_session_key_msb = bytearray(
    [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
     0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

ttn_region = "EU" # 868 MHz
ttn_config = adafruit_tinylora.TTN(
    ttn_dev_address_msb, 
    ttn_net_session_key_msb, 
    ttn_app_session_key_msb, 
    ttn_region)

lora = adafruit_tinylora.TinyLoRa(spi, cs, irq, rst, ttn_config)

while True:
    print("Sending packet...")
    order = 'big'
    data = bytearray(b"\x68\x65\x6c\x6c\x6f") # "hello"
    lora.send_data(data, len(data), lora.frame_counter)
    lora.frame_counter += 1
    print("done.")
    time.sleep(30)
