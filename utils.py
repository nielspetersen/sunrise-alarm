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

    def __init__(self, pixel_pin, num_leds=24, pixel_order=neopixel.GRB):
        """ Virtually private constructor """
        if LEDRing.__instance != None:
            raise Exception("Only one LEDRing instance supported")
        else:
            self.pixels = neopixel.NeoPixel(pixel_pin, num_leds, brightness=0.5, auto_write=False, pixel_order=pixel_order)
            LEDRing.__instance = self

    def white(self):
        self.pixels.fill((255, 255, 255))
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

        self.fill_step(255,69, 0, sleep_time) # orange-red

        self.fill_step(255, 10, 0, sleep_time) # light-red

        self.pixels.fill((255, 0, 0)) # red
        self.pixels.show()

        self.pixels.fill((0,0,0)) # switch-off leds
        self.pixels.show()

    # Switch dimmed white light on, if led is off. 
    def nightlight(self):
        self.pixels.brightness = 0.2
        if self.switched_off():
            self.pixels.fill((255, 255, 255))
            self.pixels.show()
        else:
            self.pixels.fill((0,0,0))
            self.pixels.show()

    def fill_step(self, red, green, blue, sleep_time=0):
        # even indices
        for i in range(0, num_pixels, 2):
            self.pixels[i] = (red, green, blue)
            self.pixels.show()
            time.sleep(2)
    
        #odd indices
        for index in range(1, num_pixels, 2):
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
        advance_start_sec = (advance_start_min *60) - 1 # minus 1 to reflect delay in runtime 
        return advance_start_sec // num_steps        
    
# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
#pixel_pin = board.D18

# The number of NeoPixels
#num_pixels = 24

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
#ORDER = neopixel.GRB

#pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False,
#                           pixel_order=ORDER)


    