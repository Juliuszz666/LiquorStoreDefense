import json

with open('constants.json') as constants:
    const = json.load(constants)

with open('settings.json') as settings:
    settings = json.load(settings)

gamestate = "play"

