# Mapping of days to integers according to https://gitlab.com/doctormo/python-crontab
days = {
    'monday': 0,
    'tuesday': 1,
    'wednesday': 2,
    'thursday': 3,
    'friday': 4,
    'saturday': 5,
    'sunday': 6
}

def convertAlarmTimingToCron(day, time):
    hour, minute = time.split(':')

    return '{hour} {minute} * * {day}'.format(hour=hour, minute=minute, day=days[day])