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
    
    def get_race_time(line):
        return re.findall(r"\d+:\d+", line)[0]
    
    def get_date(date_):
        return datetime.strptime(date_, "%d %b %Y")
    
    def get_age(dates_):
        race_date, birth_date = dates_
        race_date, birth_date = get_date(race_date), get_date(birth_date)
        return divmod((race_date - birth_date).days, 365.25)

    race_time = get_race_time(line)
    
    dates = re.findall(r"\d{2} \w+ \d{4}", line)
    age = get_age(dates)

    return (age, race_time)
    
def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    found = [get_event_time(r) for r in get_data() if "Jennifer Rhines" in r]
    slowest_race_age, slowest_race_time = max(found, key=lambda x: x[1])

    def format_date(age_):
        return f"{age_[0]:.0f}y{age_[1]:.0f}d"
    
    return (format_date(slowest_race_age), slowest_race_time)

