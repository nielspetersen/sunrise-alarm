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
def get_neopixel

def white():
    pixels.fill((255, 255, 255))
    pixels.show()

def sunrise(advance_time=0):
    
    sleep_time = calc_sleeptime(advance_start_min=advance_time)
    # Set brightness to default value
    pixels.brightness = 0.5
    # Start with red
    pixels.fill((255, 0, 0))
    pixels.show()

    # light-red
    fill_step(255, 10, 0, sleep_time)

    # orange-red
    fill_step(255, 69, 0, sleep_time)

    #orange
    fill_step(255, 165, 0, sleep_time)

    #gold
    fill_step(255, 200, 0, sleep_time)  

    #yellow
    fill_step(255, 255, 0, sleep_time)

    # light-yellow
    fill_step(255, 255, 224, sleep_time)
     
    white()

def sunset(advance_time=0):
    
    sleep_time = calc_sleeptime(advance_start_min=advance_time)
    # Set brightness to default value
    pixels.brightness = 0.5
    # Start with white
    white()

    fill_step(255, 255, 224, sleep_time) # light-yellow
    
    fill_step(255, 255, 0, sleep_time) #yellow

    fill_step(255, 200, 0, sleep_time) #gold
    
    fill_step(255, 165, 0, sleep_time) #orange

    fill_step(255,69,0, sleep_time) # orange-red

    fill_step(255, 10, 0, sleep_time) # light-red

    pixels.fill((255, 0, 0)) # red

    pixels.fill((0,0,0)) # switch-off leds
    pixels.show()

# Switch dimmed white light on, if led is off. 
def nightlight(neopixel_ring):
    neopixel_ring.brightness = 0.2
    if switched_off(neopixel_ring):
        neopixel_ring.fill((255, 255, 255))
        neopixel_ring.show()
    else:
        neopixel_ring.fill((0,0,0))
        neopixel_ring.show()

def fill_step(red, green, blue, sleep_time=0):
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
    time.sleep(sleep_time)

def switched_off(neopixel_ring):
    switched_off = True
    for pixel in neopixel_ring:
        if pixel != (0,0,0):
            switched_off = False
    return switched_off

def calc_sleeptime(num_steps=6, advance_start_min):
    advance_start_sec = (advance_start_min *60) - 1 # minus 1 to reflect delay in runtime 
    return advance_start_sec // num_steps
    