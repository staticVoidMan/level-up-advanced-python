from collections import namedtuple
import re

with open('specifications.txt', 'rt') as file:
    specifications = file.read()

specs = namedtuple('specs', 'range regex')
#specs range builtin module
#specs regex from re.compile

def get_linkedin_dict():
    '''Convert specifications into a dict where:
       keys: feature
       values: specs namedtuple'''
    data = {}
    minimum, maximum = (0, 0)
    regex = ""
    
    for idx, line in enumerate(specifications.splitlines()):
        try:
            key, value = line.split(':')
            key = key.strip()
            value = value.strip()
        except:
            key, value = ("", "")
        
        if key == "feature":
            feature = value
        elif key == "requirements":
            minimum, maximum = re.findall(r'\d+', value)
            minimum = int(minimum)
            maximum = int(maximum)
        elif key == "permitted characters":
            regex = ''.join(value.split())
            regex = re.compile(rf'^[{regex}]+$')
        elif key == "login characters":
            regex = ''.join(value.split()).replace(".", "\\.")
            regex = re.compile(rf'^[{regex}]+@[{regex}]+\.(com|net|org)$')
        else:
            data[feature] = specs(range(minimum, maximum + 1), regex)
    return data

def check_linkedin_feature(feature_text, url_or_login):
    '''Raise a ValueError if the url_or_login isn't login or custom_url
       If feature_text is valid, return True otherwise return False'''
    rules = get_linkedin_dict()
    rule = rules.get(url_or_login, None)
    if rule is None:
        raise ValueError('Feature needs to be either login or custom_url')
    else:
        length = len(feature_text) in rule.range
        regex = rule.regex.search(feature_text)
        return length & bool(regex)
