import board
import busio
import digitalio
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
wifi = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while not wifi.is_connected:
    print("\nConnecting to Wi-Fi...")
    try:
        wifi.connect_AP(wifi_ssid, wifi_password)
    except RuntimeError as e:
        print("Cannot connect to Wi-Fi", e)
        continue

print("Wi-Fi connected to", str(wifi.ssid, "utf-8"))
print("IP address", wifi.pretty_ip(wifi.ip_address))

# MQTT setup
mqtt_broker = "test.mosquitto.org"
mqtt_topic = "hello"

def handle_connect(client, userdata, flags, rc):
    print("Connected to {0}".format(client.broker))
    mqtt_client.subscribe(mqtt_topic)

def handle_subscribe(client, userdata, topic, granted_qos):
    print("Subscribed to {0} with QOS {1}".format(topic, granted_qos))

def handle_message(client, topic, message):
    print("Received on {0}: {1}".format(topic, message))

adafruit_minimqtt.set_socket(adafruit_esp32spi_socket, wifi)

mqtt_client = adafruit_minimqtt.MQTT(broker=mqtt_broker, is_ssl=False)

# Set callback handlers
mqtt_client.on_connect = handle_connect
mqtt_client.on_subscribe = handle_subscribe
mqtt_client.on_message = handle_message

print("\nConnecting to {0}".format(mqtt_broker))
mqtt_client.connect()

while True:
    mqtt_client.loop()