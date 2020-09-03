import board
import busio
import digitalio
import time
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_socket
import adafruit_requests as requests

# TODO: Set your Wi-Fi ssid, password
ssid = "MY_SSID"
password = "MY_PASSWORD"

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
wifi = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

def ensure_wifi_is_connected():
    while not wifi.is_connected:
        print("\nConnecting...")
        try:
            wifi.connect_AP(ssid, password)
            print("Connected to", str(wifi.ssid, "utf-8"))
            print("IP address", wifi.pretty_ip(wifi.ip_address))
        except RuntimeError as e:
            print("Cannot connect", e)
            continue

requests.set_socket(adafruit_esp32spi_socket, wifi)

while True:
    ensure_wifi_is_connected()
    try:
        response = requests.get("http://tmb.gr/hello.json") # throws RuntimeError
        json = response.json() # throws ValueError
        response.close()
    except RuntimeError as re:
        print("Request failed:", re)
    except ValueError as ve:
        print("Reading JSON failed:", ve)
    time.sleep(5)