import board
import busio
import digitalio
import time
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_socket
import adafruit_requests

# TODO: Set your Wi-Fi ssid, password
WIFI_SSID = "MY_SSID"
WIFI_PASSWORD = "MY_PASSWORD"

# ThingSpeak settings
TS_WRITE_API_KEY = "MY_WRITE_API_KEY"
TS_HTTP_SERVER = "api.thingspeak.com"

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while not esp.is_connected:
    print("\nConnecting to Wi-Fi...")
    try:
        esp.connect_AP(WIFI_SSID, WIFI_PASSWORD)
    except RuntimeError as e:
        print("Cannot connect to Wi-Fi", e)
        continue

print("Wi-Fi connected to", str(esp.ssid, "utf-8"))
print("IP address", esp.pretty_ip(esp.ip_address))


# Initialize HTTP POST client
adafruit_requests.set_socket(adafruit_esp32spi_socket, esp)


try:
    # Some test data
    humidity = 55
    temperature = 25

    # Setup server url
    post_url = "https://" + TS_HTTP_SERVER + "/update"
    # Create payload
    payload = "api_key=" + TS_WRITE_API_KEY + "&field1=" + \
        str(temperature)+"&field2="+str(humidity)

    # Send a single message
    response = adafruit_requests.post(post_url, data=payload)

    # Print the http status code; should be 200
    print(response.status_code)

    response.close()
except RuntimeError as error:
    print(error)
