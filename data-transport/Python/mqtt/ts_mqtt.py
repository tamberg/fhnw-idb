import paho.mqtt.publish as publish

# ThingSpeak settings
channelID = "MY_CHANNEL_ID"
writeAPIKey = "MY_WRITE_API_KEY"
mqttHost = "mqtt.thingspeak.com"


def main():
    try:
        # Some test data
        humidity = 54
        temperature = 27
        print("temp={:g}C humidity={:g}%".format(temperature, humidity))

        # Publish payload as MQTT message
        topic = "channels/" + channelID + "/publish/" + writeAPIKey
        payload = "field1="+str(temperature)+"&field2="+str(humidity)
        # Publish a single message to a broker, then disconnect cleanly
        publish.single(topic, payload, hostname=mqttHost)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
