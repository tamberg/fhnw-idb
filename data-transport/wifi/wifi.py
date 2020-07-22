import network
import time

ssid = b'Bitw\xc3\xa4scherei-Bau'
pwrd = b'clubmate42'

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.scan()
wifi.connect(ssid, pwrd)

conn = wifi.isconnected()
while not conn:
    print(conn)
    time.sleep(1)
    conn = wifi.isconnected()

print(wifi.ifconfig())

# ...
