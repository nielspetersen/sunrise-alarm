# -*- coding: utf-8 -*-
"""
Main script for triggering sunset / sunrise features
@author: Niels Petersen
"""
import warnings
import alarm
import sys
import digitalio
import board
import RPi.GPIO as GPIO

button1 = None
controller = alarm.Alarm(sound_support=False)

def initializeButton():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(12, GPIO.RISING, callback=stopSunrise, bouncetime=250)

def stopSunrise(channel):
    controller.black()
    exit(0)

def main():
    #default action if not provided
    action = '--sunrise'
    # default advance or lead time to start sunrise or sunset mode in minutes
    advance = 30

    # read parameters from shell/bash input
    if len(sys.argv) >= 2:
        action = sys.argv[1]
        if len(sys.argv) >= 3:
            advance = int(sys.argv[2])

    # controller = alarm.Alarm(sound_support=False)
    initializeButton()

    if action == '--sunrise':
        controller.sunrise(advance_time=advance)
    elif action == '--sunset':
        controller.sunset(advance_time=advance)
    elif action == '--nightlight':
        controller.nightlight()

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    main()