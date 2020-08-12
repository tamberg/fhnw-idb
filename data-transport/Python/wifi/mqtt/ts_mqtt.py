import paho.mqtt.publish as publish

# ThingSpeak settings
TS_CHANNEL_ID = "MY_CHANNEL_ID"
TS_WRITE_API_KEY = "MY_WRITE_API_KEY"
TS_MQTT_HOST = "mqtt.thingspeak.com"


# Some test data
humidity = 54
temperature = 27
print("temp={:g}C humidity={:g}%".format(temperature, humidity))

# Publish payload as MQTT message
topic = "channels/" + TS_CHANNEL_ID + "/publish/" + TS_WRITE_API_KEY
payload = "field1="+str(temperature)+"&field2="+str(humidity)
publish.single(topic, payload, hostname=TS_MQTT_HOST)
