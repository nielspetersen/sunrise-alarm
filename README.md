# Prerequisites:
  Download Raspbian image and burn image to SD card
  
  Change localization / time zone:
  
  ```sh
  sudo raspi-config
  
  # And use the following settings 
  Select 4 / "Localisation Options" 
  Select "I2 Change Timezone"
  Select "Continent" and choose your continent
  Select "Nearest City" and choose your closest city from the list 
  ```

# Software-Installation 
(based on https://learn.adafruit.com/circuitpython-on-raspberrypi-linux?view=all):

1. Update / Upgrade Raspbian

    `sudo apt-get update`

    or

    `sudo apt-get upgrade`

2. Install Python 3

    `sudo apt-get install python3-pip`
  
3. Enable I2C 
(https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

4. Enable SPI (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-spi)

5. Verifiy I2C and SPI devices via

    `ls /dev/i2c* /dev/spi*`
  
6. Install Raspberry Pi libraray GPIO

    `pip3 install RPI.GPIO`
  
7. Install blinka library for supporting differenct python api 

    `pip3 install adafruit-blinka`
  
8. Verify blinka installation with new file:

```python   
# in file blinkatest.py

import board
import digitalio
import busio

print("Hello blinka!")

# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")

# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")

# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

print("done!")
```

9. Setup for LCD usage
- https://learn.adafruit.com/character-lcds/python-circuitpython

  e.g. via `sudo pip3 install adafruit-circuitpython-charlcd`

10. Install Apache web server
11. Install PHP 7.x
12. Customize the PHP script for writing new alarm time into CSV /txt file

  By default the alarm time will be stored and read from:

      /var/www/html/data/alarm_time.csv

13. Verify that crontab is installed (also for python)

    `sudo pip3 install python-crontab`

13. Install incron for updating cronjob for triggering python script after changing alarm time

    `sudo apt-get install incron`

14. Show Time and IP on boot for debugging
https://learn.adafruit.com/drive-a-16x2-lcd-directly-with-a-raspberry-pi/init-script
see boot_info.py for actual source code

15. Change file owner for alarm_time storage file
sudo chown www-data:incron alarm_time.txt
    
16. Define incron for listing on alarm_time.txt file
Open session with user of desire and execute the following commands: 

```sh
cd ~
incrontab -e

# Add to file
/var/www/html/data/alarm_time.csv IN_MODIFY /home/pi/update_cron.py
```
