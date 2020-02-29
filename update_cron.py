from crontab import CronTab
import os
import csv
import datetime as dt
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# Get access to Cron
cron = CronTab(user='pi') 

existing_job = cron.find_comment("sunrise_alarm") 

if existing_job:
    cron.remove(existing_job)

job = cron.new(command='sudo python sunrise.py', comment='sunrise_alarm')

with open('/var/www/html/data/alarm_time.txt','r') as txtfile:
    line = txtfile.readline()
    
    if line:
        alarm_time = dt.datetime.strptime(line, "%Y-%m-%dT%H:%M")

        lcd_rs = digitalio.DigitalInOut(board.D26)
        lcd_en = digitalio.DigitalInOut(board.D19)
        lcd_d7 = digitalio.DigitalInOut(board.D27)
        lcd_d6 = digitalio.DigitalInOut(board.D22)
        lcd_d5 = digitalio.DigitalInOut(board.D24)
        lcd_d4 = digitalio.DigitalInOut(board.D25)

        lcd_columns = 16
        lcd_rows = 2

        lcd = characterlcd.Character_LCD_Mono(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows)

        message = 'Weckzeit {hour}:{minute}'.format(hour=alarm_time.hour, minute=alarm_time.minute)
        print(message)

        lcd.message = message
        lcd.cursor = False
    else:
        print("File is empty")
# read time from file 
# set cron due time to value in file
# https://pypi.org/project/python-crontab/