import json

with open('json/constants.json', 'r') as constants:
    const = json.load(constants)

with open('json/settings.json', 'r') as options:
    settings = json.load(options)

def get_username():
    return settings['USERNAME']

def save_username(text):
    settings['USERNAME'] = text
    with open('json/settings.json', 'w') as file:
        json.dump(settings, file, indent=2)