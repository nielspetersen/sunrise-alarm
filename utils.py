import datetime

# Mapping of days to integers according to https://gitlab.com/doctormo/python-crontab
days = {
    'monday': 1,
    'tuesday': 2,
    'wednesday': 3,
    'thursday': 4,
    'friday': 5,
    'saturday': 6,
    'sunday': 0
}

def convertAlarmTimingToCron(day, time, advance):
    hour, minute = map(int, time.split(':'))
    # Create datetime object to benefit from builtin calculations with timedelta
    alarmtime = datetime.datetime.now()
    alarmtime = alarmtime.replace(hour=hour, minute=minute) # set to predefined alarm time
    alarmtime = alarmtime - datetime.timedelta(minutes=advance) # subtract the advance start time

    return '{minute} {hour} * * {day}'.format(minute=alarmtime.minute, hour=alarmtime.hour, day=days[day])