# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

class LEDRing:
    __instance = None

    @staticmethod
    def getInstance():
        if LEDRing.__instance != None:
            LEDRing()
        return LEDRing.__instance

    def __init__(self, pixel_pin=board.D18, num_leds=24, pixel_order=neopixel.GRB):
        """ Virtually private constructor """
        if LEDRing.__instance != None:
            raise Exception("Only one LEDRing instance supported")
        else:
            self.num_pixels = num_leds
            self.pixel_pin = pixel_pin
            self.pixel_order = pixel_order
            self.pixels = neopixel.NeoPixel(pixel_pin, num_leds, brightness=0.5, auto_write=False, pixel_order=pixel_order)
            LEDRing.__instance = self

    # Switch all LEDs to white color
    def white(self, brightness=0.5):
        self.pixels.brightness = brightness
        self.pixels.fill((255, 255, 255))
        self.pixels.show()

    # Switch off all LEDs 
    def black(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()

    def sunrise(self, advance_time=0):
        
        sleep_time = self.__calc_sleeptime(advance_start_min=advance_time)
        # Set brightness to default value
        self.pixels.brightness = 0.5
        # Start with red
        self.pixels.fill((255, 0, 0))
        self.pixels.show()

        # light-red
        self.fill_step(255, 10, 0, sleep_time)

        # orange-red
        self.fill_step(255, 69, 0, sleep_time)

        #orange
        self.fill_step(255, 165, 0, sleep_time)

        #gold
        self.fill_step(255, 200, 0, sleep_time)  

        #yellow
        self.fill_step(255, 255, 0, sleep_time)

        # light-yellow
        self.fill_step(255, 255, 224, sleep_time)
        
        white()

    def sunset(self, advance_time=0):
        
        sleep_time = self.__calc_sleeptime(advance_start_min=advance_time)
        # Set brightness to default value
        self.pixels.brightness = 0.5
        # Start with white
        self.white()

        self.fill_step(255, 255, 224, sleep_time) # light-yellow
        
        self.fill_step(255, 255, 0, sleep_time) #yellow

        self.fill_step(255, 200, 0, sleep_time) #gold
        
        self.fill_step(255, 165, 0, sleep_time) #orange

        self.fill_step(255, 69, 0, sleep_time) # orange-red

        self.fill_step(255, 10, 0, sleep_time) # light-red

        self.pixels.fill((255, 0, 0)) # red
        self.pixels.show()

        self.black() # switch-off leds

    # Switch dimmed white light on, if led is off. 
    def nightlight(self):
        if self.switched_off():
            self.white(brightness=0.2)
        else:
            self.black()

    def fill_step(self, red, green, blue, sleep_time=0):
        # even indices
        for i in range(0, self.num_pixels, 2):
            self.pixels[i] = (red, green, blue)
            self.pixels.show()
            time.sleep(2)
    
        #odd indices
        for index in range(1, self.num_pixels, 2):
            self.pixels[index] = (red, green, blue)
            self.pixels.show()
            time.sleep(2)
        time.sleep(sleep_time)

    def switched_off(self):
        switched_off = True
        for pixel in self.pixels:
            if pixel != (0, 0, 0):
                switched_off = False
        return switched_off

    def __calc_sleeptime(self, num_steps=6, advance_start_min=30):
        sleeptime = 0
        if advance_start_min >= 1:
            advance_start_sec = (advance_start_min * 60) - 1 # minus 1 to reflect delay in runtime 
            sleeptime = advance_start_sec // num_steps
        return sleeptime        

    