# Based on https://github.com/adafruit/Adafruit_CircuitPython_TinyLoRa licensed under LGPL (!)

import time
import analogio
import board
import busio
import digitalio
from adafruit_tinylora import adafruit_tinylora

sensor = analogio.AnalogIn(board.A0) # nRF52840 A0, Grove A0

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)

# FeatherWing RFM95, nRF52840
cs = digitalio.DigitalInOut(board.D5)
irq = digitalio.DigitalInOut(board.D10)
rst = digitalio.DigitalInOut(board.D6)

# TODO: App > Device > Settings (ABP) from
# TTN https://console.thethingsnetwork.org/
ttn_dev_address_msb = bytearray([0x26, 0x01, 0x1F, 0x69])

ttn_net_session_key_msb = bytearray(
    [0x62, 0xB3, 0x93, 0x1D, 0xB0, 0x26, 0xDA, 0x37, 
     0x19, 0xBF, 0x10, 0x55, 0x83, 0x22, 0xD5, 0xF9])

ttn_app_session_key_msb = bytearray(
    [0x3C, 0x42, 0x35, 0xB6, 0xFC, 0x3F, 0x58, 0x76, 
     0x3C, 0x8C, 0x34, 0xE2, 0x33, 0x23, 0xDD, 0xA1])

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
    data = sensor.value.to_bytes(2, order)
    # or = bytearray(b"\x04\x00")
    lora.send_data(data, len(data), lora.frame_counter)
    lora.frame_counter += 1
    print("done.")
    time.sleep(30)
