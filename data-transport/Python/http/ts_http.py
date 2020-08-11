import urllib.request

# ThingSpeak settings
writeAPIKey = "MY_WRITE_API_KEY"
httpHost = "api.thingspeak.com"


def main():
    try:
        # Some test data
        humidity = 51
        temperature = 26
        print("temp={:g}C humidity={:g}%".format(temperature, humidity))

        # Send payload as HTTP GET request
        url = "http://" + httpHost + "/update"
        payload = "field1=" + str(temperature) + "&field2=" + str(humidity)
        thingspeak = url + "?api_key=" + writeAPIKey + "&" + payload
        response = urllib.request.urlopen(url=thingspeak)

        # Print response; should be 200 (= OK)
        print(response.status)

    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
