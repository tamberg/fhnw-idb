import board
import busio
import digitalio
import time
from adafruit_esp32spi import adafruit_esp32spi
from adafruit_esp32spi import adafruit_esp32spi_socket
from adafruit_minimqtt import adafruit_minimqtt

# TODO: Set your Wi-Fi ssid, password
wifi_ssid = "MY_SSID"
wifi_password = "MY_PASSWORD"

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while not esp.is_connected:
    print("\nConnecting to Wi-Fi...")
    try:
        esp.connect_AP(wifi_ssid, wifi_password)
    except RuntimeError as e:
        print("Cannot connect Wi-Fi", e)
        continue

print("Wi-Fi connected to", str(esp.ssid, "utf-8"))
print("IP address", esp.pretty_ip(esp.ip_address))

# MQTT setup
mqtt_broker = "test.mosquitto.org"
mqtt_topic = "hello"

def handle_connect(client, userdata, flags, rc):
    print("Connected to {0}".format(client.broker))

def handle_publish(client, userdata, topic, pid):
    print("Published to {0} with PID {1}".format(topic, pid))

adafruit_minimqtt.set_socket(adafruit_esp32spi_socket, esp)

mqtt_client = adafruit_minimqtt.MQTT(broker=mqtt_broker, is_ssl=False)

# Set callback handlers
mqtt_client.on_connect = handle_connect
mqtt_client.on_publish = handle_publish

print("\nConnecting to {0}".format(mqtt_broker))
mqtt_client.connect()

while True:
    t = time.monotonic()
    mqtt_message = "Hello, up for {0}s".format(t)
    mqtt_client.publish(mqtt_topic, mqtt_message)
    time.sleep(5)
