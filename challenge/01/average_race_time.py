# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime

def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.read()
    return content

def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data().split("\n")
    search_str = "Jennifer Rhines"
    filtered_races = [r.split()[0] for r in races if search_str in r]
    return filtered_races

def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    seconds = 0.0
    for r in racetimes:
        r = r.split(":")
        seconds += int(r[0]) * 60
        seconds += float(r[1])
    
    seconds /= len(racetimes)
    minutes = seconds // 60
    seconds = seconds % 60

    return f"{minutes:.0f}:{seconds:.1f}"