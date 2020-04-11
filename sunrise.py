# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 24

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5, auto_write=False,
                           pixel_order=ORDER)

def white():
    pixels.fill((255, 255, 255))
    pixels.show()

def sunrise():
    # Start with red
    pixels.fill((255, 0, 0))

    # light-red
    fill_step(255, 10, 0)

    # orange-red
    fill_step(255,69,0)

    #orange
    fill_step(255, 165, 0)

    #gold
    fill_step(255, 215, 0)

    #yellow
    fill_step(255, 255, 0)

    # light-yellow
    fill_step(255, 255, 224)
     
    white()

def fill_step(red, green, blue):
    # even indices
    for i in range(0, num_pixels, 2):
        pixels[i] = (red, green, blue)
        pixels.show()
        time.sleep(2)
   
    #odd indices
    for index in range(1, num_pixels, 2):
        pixels[index] = (red, green, blue)
        pixels.show()
        time.sleep(2)

while True:
    sunrise()
