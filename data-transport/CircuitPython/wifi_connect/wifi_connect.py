import board
import busio
import digitalio
from adafruit_esp32spi import adafruit_esp32spi # :)

ssid = "MY_SSID"
password = "MY_PASSWORD"

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while not esp.is_connected:
    print("\nConnecting...")
    try:
        esp.connect_AP(ssid, password)
    except RuntimeError as e:
        print("Cannot connect", e)
        continue

print("Connected to", str(esp.ssid, "utf-8"))
print("IP address", esp.pretty_ip(esp.ip_address))
