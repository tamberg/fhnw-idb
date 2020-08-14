import board
import busio
import digitalio
from adafruit_esp32spi import adafruit_esp32spi # :)

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while True:
    print("\nScanning...")
    networks = esp.scan_networks()
    for network in networks:
    	rssi = network['rssi']
    	ssid = str(network['ssid'], 'utf-8')
        print("  rssi: %d, ssid: %s" % (rssi, ssid))
