def connect_wlan():
    # Connect to WLAN
    import network

    ssid      = "CBOX"
    password  =  "nus2DNApoint"

    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("WLAN already connected")
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("WLAN connection successful")

def disconnect_wlan():
    import network
    station = network.WLAN(network.STA_IF)
    station.disconnect()
    station.active(False)
