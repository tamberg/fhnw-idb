# MicroPython 

## Developing with MicroPython

- Using the MU-Editor which can be downloaded from https://codewith.mu/
    - NOTE für Mac User with Catalina OSX  
        Start the application for the first time with CTRL Key pressed to be able to accept the security restrictions be the macos. Use version Mu 1.1.0.alpha.2
		
- The reference docs can be found on http://docs.micropython.org/en/latest/

- "Third Party Packages" support within mu-editor does not work under MacOS due to missing SSL/TLS support
  Work-Around:  
  pip install  --target "/Users/luthiger/Library/Application Support/mu/site-packages"

- WiFi support  
    see  https://diyprojects.io/micropython-tutorial-manage-wifi-connection-startup-esp8266-esp32/

- Using WebREPL to download files to the ESP8266 board  
    see https://docs.micropython.org/en/latest/esp32/quickref.html#webrepl-web-browser-interactive-prompt
