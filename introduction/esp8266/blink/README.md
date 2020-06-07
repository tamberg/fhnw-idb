# Blink App

## Challenge

The small application in `main.py` toggles the onboard led (red) endlessly. You can test this application using the **MU-Editor**. But the application is not persistently stored on the board. After a reboot the code is lost.

**Question: How it possible to run own code even after rebooting the board?**

## Solution

You will use the [**WebREPL**](https://docs.micropython.org/en/latest/esp8266/quickref.html#webrepl-web-browser-interactive-prompt) to connect to the board and to download files on to the board. Use the hosted web application under [http://micropython.org/webrepl/](http://micropython.org/webrepl/) to access the WebUI and to be able to open the WebSocket connection to the board.

Follow these steps:

1. Understand the [boot process](https://docs.micropython.org/en/latest/esp8266/general.html#boot-process).

2. Read the chapter about [WiFi](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#wifi) support on the ESP8622. Your ESP8622 board must act as a WiFi access point (AP).

3. Start the **MU-Editor** and open the REPL console.

3. Activate, enable and start the [WebREPL](https://docs.micropython.org/en/latest/esp8266/quickref.html#webrepl-web-browser-interactive-prompt) User Interface.   
   You should see the following message in the REPL of the MU-Editor: 

   ```
   on ws://192.168.4.1:8266
   Started webrepl in normal mode
   ```

   It indicates that the WebREPL daemon is started and is able to listen for WebSocket connections requests on port 8266. To connect to this daemon, you have to use the URL `ws://192.168.4.1:8266`.

3. Connect your host computer to the ESP8622 Wifi network `MicroPython-xxx`. 

4. Connect the WebREPL to the board. See following figure:

<img src="webrepl.png">

4. Load and send the file `main.py` to the board, using the WebREPL User Interface (see above).

5. Reboot/reconnect the board. 

6. **Does it blink?**

## Hints

To structure your application, you can place your code in different `*.py` files. Only the names `boot.py` and `main.py` are reserved (see [Boot Process](https://docs.micropython.org/en/latest/esp8266/general.html#boot-process)).

**Example**: 

Place your application code into a file named `app.py`:

```python
from machine import Pin
import time

def blink():
    led = Pin(0, Pin.OUT)     # create output pin on GPIO0 (red led on board!)
    val = True                # initialize pin

    while True:               # loop forever
        led.value(val)        # set value on/off
        val = not val         # toggle value
        time.sleep_ms(100)    # wait
```

Start your application after booting, calling the function `blink()`:

```python
import app

app.blink()
```

Send both files to the ESP8222 board by using [**WebREPL**](https://docs.micropython.org/en/latest/esp8266/quickref.html#webrepl-web-browser-interactive-prompt).
