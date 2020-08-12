import board
import busio
import digitalio
import sys
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
import adafruit_minimqtt.adafruit_minimqtt as MQTT

# TODO: Set your Wi-Fi ssid, password
WIFI_SSID = "YOUR_SSID"
WIFI_PASSWORD = "YOUR_PASSWORD"

# TODO: Set your ThingSpeak settings
TS_CHANNEL_ID = "YOUR_CHANNEL_ID"
TS_WRITE_API_KEY = "YOUR_WRITE_API_KEY"
TS_MQTT_HOST = "mqtt.thingspeak.com"

# FeatherWing ESP32 AirLift, nRF52840
cs = digitalio.DigitalInOut(board.D13)
rdy = digitalio.DigitalInOut(board.D11)
rst = digitalio.DigitalInOut(board.D12)
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, cs, rdy, rst)

while not esp.is_connected:
    print("\nConnecting to WLAN...")
    try:
        esp.connect_AP(WIFI_SSID, WIFI_PASSWORD)
    except RuntimeError as e:
        print("Cannot connect", e)
        continue

print("Connected to", str(esp.ssid, "utf-8"))
print("IP address", esp.pretty_ip(esp.ip_address))


# Initialize MQTT interface with the esp interface
MQTT.set_socket(socket, esp)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=TS_MQTT_HOST
)

try:
    # Connect to ThingSpeak
    mqtt_client.connect()
    mqtt_client.loop()
    print("Connected to", mqtt_client.broker)

    # Some test data
    humidity = 55
    temperature = 25
    print("temp={:g}C humidity={:g}%".format(temperature, humidity))

    # Publish payload as MQTT message
    topic = "channels/" + TS_CHANNEL_ID + "/publish/" + TS_WRITE_API_KEY
    payload = "field1="+str(temperature)+"&field2="+str(humidity)

    # Publish a single message to a broker, then disconnect cleanly
    mqtt_client.publish(topic, payload)
    mqtt_client.disconnect()

except MQTT.MMQTTException as error:
    print(error)
    sys.exit()
