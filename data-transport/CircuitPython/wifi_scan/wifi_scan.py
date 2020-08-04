# Based on 

import board
import busio
import digitalio
from adafruit_esp32spi import adafruit_esp32spi # :)

print("ESP32 SPI hardware test")

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("ESP32 found and in idle mode")

print("Firmware version", esp.firmware_version)
print("MAC addr:", [hex(i) for i in esp.MAC_address])

while True:
    print("\nScanning...");
    for ap in esp.scan_networks():
    	rssi = ap['rssi']
    	ssid = str(ap['ssid'], 'utf-8')
        print("  rssi: %d, ssid: %s" % (rssi, ssid))