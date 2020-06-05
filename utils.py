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

def convertAlarmTimingToCron(day, time):
    hour, minute = time.split(':')

    return '{minute} {hour} * * {day}'.format(minute=minute, hour=hour, day=days[day])