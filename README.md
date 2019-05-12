# Prerequisites:
  Download Raspbian image and burn image to SD card
  
  Change localization / time zone:
  
  sudo raspi-config
  Select 4 / "Localisation Options" 
  Select I2 Change Timezone
  Select "Continent"
  Select "Nearest City"

# Software-Installation (https://learn.adafruit.com/circuitpython-on-raspberrypi-linux?view=all):

1. Update / Upgrade Raspbian
  sudo apt-get update
or 
  sudo apt-get upgrade
2. Install Python 3
  sudo apt-get install python3-pip
  
3. Enable I2C (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c)

4. Enable SPI (https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-spi)

5. Verifiy I2C and SPI devices via

  ls /dev/i2c* /dev/spi*
  
6. Install Raspberry Pi libraray GPIO
  pip3 install RPI.GPIO
  
7. Install blinka library for supporting differenct python api 
  pip3 install adafruit-blinka
  
8. Verify blinka installation with new file: blinkatest.py
      
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
  
9. Install Apache web server
10. Install PHP 7.x
    
