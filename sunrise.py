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
    pixels.fill((255, 0, 0))
    #pixels.show()
    fill_step(255, 33, 0)

    #time.sleep(5)
    #pixels.fill((255, 77, 0))
    #pixels.show()
    fill_step(255, 65, 0)

    #time.sleep(5)
    #pixels.fill((255, 103, 0))
    #pixels.show()
    fill_step(255, 103, 0)

    fill_step(0, 0, 255)

    fill_step(0, 255, 0)
    #pixels.fill((255, 129, 0))
    #pixels.show()
    #time.sleep(5)

    fill_step(255, 167, 0)
    #pixels.fill((255, 167, 0))
    #pixels.show()

    #pixels.fill((255, 255, 255))
    #pixels.show()
     
    white()

def fill_step(green, red, blue):
    # even indices
    for i in range(0, num_pixels, 2):
        pixels[i] = (green, red, blue)
        pixels.show()
        time.sleep(2)
   
    #odd indices
    for index in range(1, num_pixels, 2):
        pixels[index] = (green, red, blue)
        pixels.show()
        time.sleep(2)

while True:
    sunrise()
