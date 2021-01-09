import alarm
import RPi.GPIO as GPIO
import multiprocessing

# Get singleton main alarm object
controller = alarm.Alarm(sound_support=False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def nightlightCallback(channel):
    controller.nightlight()

def sunsetCallback(channel):
    controller.sunset(20)
    
#GPIO.add_event_detect(16, GPIO.RISING, callback=nightlightCallback, bouncetime=250)
#GPIO.add_event_detect(23, GPIO.RISING, callback=sunsetCallback, bouncetime=250)

# infinite loop
try: 
    process_nightlight = multiprocessing.Process(target=controller.nightlight)
    process_sunset = multiprocessing.Process(target=controller.sunset, args=(20,))
    while True:
        button_nightlight = GPIO.input(16)
        button_sunset = GPIO.input(23)

        if GPIO.input(16) == GPIO.HIGH:
            #controller.nightlight()
            if process_nightlight.is_alive():
                controller.nightlight()
            else:
                if process_sunset.is_alive():
                    process_sunset.terminate()
                    process_sunset.join()
                process_nightlight.start()

        elif GPIO.input(23) == GPIO.HIGH:
            if process_sunset.is_alive(): 
                process_sunset.terminate()
                process_sunset.join()
            else: 
                if process_nightlight.is_alive():
                    process_nightlight.terminate()
                    process_nightlight.join()
                process_sunset.start()

except KeyboardInterrupt:
    GPIO.cleanup()