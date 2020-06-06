#!/usr/bin/python

from crontab import CronTab
import os
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd
import logging
import json
import utils

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

# Get access to Cron
cron = CronTab(user='pi') 

# Clear all existing cron jobs
cron.remove_all()

#existing_job = cron.find_comment("sunrise_alarm") 
#if existing_job:
#    cron.remove(existing_job)

with open('/var/www/html/data/alarms.json','r') as jsonfile:
    data = json.load(jsonfile)
    for day, alarm in data['alarms'].items():
        # only consider days with active alarms
        if alarm['active'] == True:
            advance = int(alarm['advance_start'])
            job = cron.new(command='sudo python main.py --sunrise {}'.format(advance), comment='sunrise_alarm')
            
            time = alarm['time_utc']
            timing = utils.convertAlarmTimingToCron(day, time, advance)
            job.setall(timing)

cron.write()