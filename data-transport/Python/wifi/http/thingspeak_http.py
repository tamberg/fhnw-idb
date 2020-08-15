import urllib.request

# ThingSpeak settings
TS_WRITE_API_KEY = "MY_WRITE_API_KEY"
TS_HTTP_HOST = "api.thingspeak.com"


# Some test data
humidity = 51
temperature = 26
print("temp={:g}C humidity={:g}%".format(temperature, humidity))

# Send payload as HTTP GET request
url = "http://" + TS_HTTP_HOST + "/update"
payload = "field1=" + str(temperature) + "&field2=" + str(humidity)
thingspeak = url + "?api_key=" + TS_WRITE_API_KEY + "&" + payload
response = urllib.request.urlopen(url=thingspeak)

# Print response; should be 200 (= OK)
print(response.status)
