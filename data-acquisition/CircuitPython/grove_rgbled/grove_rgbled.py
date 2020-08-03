// Based on https://github.com/DexterInd/GrovePi/tree/master/Software/Python/grove_chainable_rgb_led licensed under MIT License

import board
import digitalio
import time

CLK_PIN = board.D5 # nRF5840 D5, Grove D2
DATA_PIN = board.D6
NUMBER_OF_LEDS = 1

class ChainableLED():
    def __init__(self, clk_pin, data_pin, number_of_leds):
        self.__clk_pin = digitalio.DigitalInOut(clk_pin)
        self.__data_pin = digitalio.DigitalInOut(data_pin)
        self.__number_of_leds = number_of_leds
 
        self.__clk_pin.direction = digitalio.Direction.OUTPUT
        self.__data_pin.direction = digitalio.Direction.OUTPUT
 
        for i in range(self.__number_of_leds):
            self.setColorRGB(i, 0, 0, 0)
 
    def clk(self):
        self.__clk_pin.value = False
        time.sleep(0.00002)
        self.__clk_pin.value = True
        time.sleep(0.00002)
 
    def sendByte(self, b):
        # Send one bit at a time, starting with the MSB
        for i in range(8):
            # If MSB is 1, write one and clock it, else write 0 and clock
            if (b & 0x80) != 0:
                self.__data_pin.value = True
            else:
                self.__data_pin.value = False
            self.clk()
 
            # Advance to the next bit to send
            b = b << 1
 
    def sendColor(self, red, green, blue):
        # Start by sending a byte with the format '1 1 /B7 /B6 /G7 /G6 /R7 /R6' 
        #prefix = B11000000
        prefix = 0xC0
        if (blue & 0x80) == 0:     
            #prefix |= B00100000
            prefix |= 0x20
        if (blue & 0x40) == 0:     
            #prefix |= B00010000
            prefix |= 0x10
        if (green & 0x80) == 0:    
            #prefix |= B00001000
            prefix |= 0x08
        if (green & 0x40) == 0:    
            #prefix |= B00000100
            prefix |= 0x04
        if (red & 0x80) == 0:      
            #prefix |= B00000010
            prefix |= 0x02
        if (red & 0x40) == 0:      
            #prefix |= B00000001
            prefix |= 0x01
        self.sendByte(prefix)
 
        # Now must send the 3 colors
        self.sendByte(blue)
        self.sendByte(green)
        self.sendByte(red)
 
    def setColorRGB(self, led, red, green, blue):
        # Send data frame prefix (32x '0')
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
 
        # Send color data for each one of the leds
        for i in range(self.__number_of_leds):
            self.sendColor(red, green, blue)
 
        # Terminate data frame (32x "0")
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)
        self.sendByte(0x00)


if __name__ == "__main__":
    rgb_led = ChainableLED(CLK_PIN, DATA_PIN, NUMBER_OF_LEDS)

    while True:
        # The first parameter: NUMBER_OF_LEDS - 1; Other parameters: the RGB values.
        rgb_led.setColorRGB(0, 255, 0, 0)
        time.sleep(1)
        rgb_led.setColorRGB(0, 0, 255, 0)
        time.sleep(1)
        rgb_led.setColorRGB(0, 0, 0, 255)
        time.sleep(1)
