# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days

import re
from datetime import datetime, timedelta

def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    
    found = tuple()
    if "Jennifer Rhines" in line:
        racetime_parts = re.findall(r"\d+:\d+", line)[0].split(":")
        race_time = timedelta(minutes = int(racetime_parts[0]), 
                              seconds = int(racetime_parts[1]))
        dates = [datetime.strptime(d, "%d %b %Y") for d in re.findall(r"\d{2} \w+ \d{4}", line)]
        difference = (dates[0] - dates[1])
        found = (difference, race_time)
    return found
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    times = []
    for r in get_data():
        t = get_event_time(r)
        if len(t) > 0:
            times.append(t)
    slowest = sorted(times, key=lambda x: x[1])[-1]
    years, days = divmod(slowest[0].days, 365.25)
    
    age = f"{years:.0f}y{days:.0f}d"
    time = f"{slowest[1]}"[2:]
    return (age, time)

